package ee.ut.bigdata;

import com.google.gson.Gson;
import weka.classifiers.Classifier;
import weka.classifiers.evaluation.Evaluation;
import weka.core.Instances;
import weka.core.converters.ConverterUtils;
import weka.filters.Filter;
import weka.filters.unsupervised.attribute.NumericToNominal;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public abstract class WekaBenchmark<C extends Classifier> implements Benchmark {

	@Override
	public void benchmark(String dataset, String output, int timeLimit, float split) {
		Instances data = loadInstances(dataset);
		if (data == null)
			return;

		data.randomize(new Random());
		int trainSize = Math.round(data.numInstances() * split);
		int testSize = data.numInstances() - trainSize;
		Instances train = new Instances(data, 0, trainSize);
		Instances test = new Instances(data, trainSize, testSize);
		C classifier = initClassifier(timeLimit);

		BenchmarkResult result = benchmarkResult(classifier, train, test, timeLimit);

		output(result, output);
	}

	protected abstract C initClassifier(int timeLimit);

	protected abstract String getBestModel(C classifier, Evaluation eval);

	private Instances loadInstances(String location) {
		try {
			ConverterUtils.DataSource source = new ConverterUtils.DataSource(location);
			Instances data = source.getDataSet();
			if (data.classIndex() == -1)
				data.setClassIndex(data.numAttributes() - 1);

			Filter convert = new NumericToNominal();
			convert.setInputFormat(data);
			data = Filter.useFilter(data, convert);

			return data;
		} catch (Exception e) {
			e.printStackTrace();
			return null;
		}
	}

	private BenchmarkResult benchmarkResult(C classifier, Instances train, Instances test, int timeLimit) {
		BenchmarkResult result = new BenchmarkResult();
		Thread trainingThread = new Thread(() -> {
			try {
				classifier.buildClassifier(train);
			} catch (InterruptedException e) {
				// Ignore
			} catch (Exception e) {
				result.setError(e.getMessage());
				e.printStackTrace();
			}
		});
		long timeStart = System.currentTimeMillis();
		long timeEnd = 0;
		try {
			trainingThread.start();
			trainingThread.join((long)(timeLimit * 60000 * 1.1));
			timeEnd = System.currentTimeMillis();

			if (trainingThread.isAlive()) {
				trainingThread.interrupt();
				result.setError("Timeout");
			} else if (result.getError() == null) {
				Evaluation eval = new Evaluation(train);
				eval.evaluateModel(classifier, test);
				result.setAccuracy(eval.pctCorrect() / 100.0);
				result.setPrecision(eval.weightedPrecision());
				result.setRecall(eval.weightedRecall());
				result.setF1score(eval.weightedFMeasure());
				result.setModel(getBestModel(classifier, eval));
			}
		} catch (Exception e) {
			result.setError(e.toString());
			e.printStackTrace();
		} finally {
			if (timeEnd == 0) {
				timeEnd = System.currentTimeMillis();
			}
			result.setTime(Math.round((timeEnd - timeStart) / 1000.0));
		}
		return result;
	}

	private void output(BenchmarkResult result, String output) {
		Gson gson = new Gson();
		String json = gson.toJson(result);
		try (BufferedWriter writer = new BufferedWriter(new FileWriter(new File(output)))) {
			writer.write(json);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
