package ee.ut.bigdata;

import com.google.gson.Gson;
import ee.ut.bigdata.impl.AutoWekaBenchmark;
import weka.classifiers.Classifier;
import weka.classifiers.evaluation.Evaluation;
import weka.core.Instances;
import weka.core.converters.ConverterUtils;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public abstract class WekaBenchmark<C extends Classifier> implements Benchmark {

	@Override
	public void benchmark(String dataset, String output, int timeLimit, int nRuns, float split) {
		Instances data = loadInstances(dataset);
		if (data == null)
			return;

		List<BenchmarkResult> results = new ArrayList<>();
		for (int i = 0; i < nRuns; ++i) {
			data.randomize(new Random());
			int trainSize = Math.round(data.numInstances() * split);
			int testSize = data.numInstances() - trainSize;
			Instances train = new Instances(data, 0, trainSize);
			Instances test = new Instances(data, trainSize, testSize);
			C classifier = initClassifier(timeLimit);
			BenchmarkResult result = benchmarkResult(classifier, train, test, timeLimit);
			results.add(result);
		}

		output(results, dataset, output);
	}

	protected abstract C initClassifier(int timeLimit);

	protected abstract String getBestModel(C classifier, Evaluation eval);

	private Instances loadInstances(String location) {
		try {
			ConverterUtils.DataSource source = new ConverterUtils.DataSource(location);
			Instances data = source.getDataSet();
			if (data.classIndex() == -1)
				data.setClassIndex(data.numAttributes() - 1);
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
		} finally {
			if (timeEnd == 0)
				timeEnd = System.currentTimeMillis();
			result.setTime(Math.round((timeEnd - timeStart) / 1000.0));
		}
		return result;
	}

	private void output(List<BenchmarkResult> results, String dataset, String output) {
		Gson gson = new Gson();
		String json = gson.toJson(results);
		try {
			String fileName = Paths.get(dataset).getFileName().toString().replaceFirst("[.][^.]+$", "") + ".json";
			File file = Paths.get(output, AutoWekaBenchmark.class.getSimpleName(), fileName).toFile();
			file.getParentFile().mkdirs();
			file.createNewFile();

			try (BufferedWriter writer = new BufferedWriter(new FileWriter(file))) {
				writer.write(json);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public void runClassifier(String[] args) {
		if (args.length < 4)
			throw new IllegalArgumentException("Not enough arguments. Usage: <dataset> <output> <timeLimit> <nRuns>");
		String dataset = args[0];
		String output = args[1];
		int timeLimit = Integer.parseInt(args[2]);
		int nRuns = Integer.parseInt(args[3]);
		float split = 0.75f;

		benchmark(dataset, output, timeLimit, nRuns, split);
	}
}
