package ee.ut.bigdata.impl;

/*
import de.upb.crc901.mlplan.multiclass.wekamlplan.MLPlanWekaBuilder;
import de.upb.crc901.mlplan.multiclass.wekamlplan.weka.WekaMLPlanWekaClassifier;
import ee.ut.bigdata.WekaBenchmark;
import ee.ut.bigdata.utils.PropertiesUtils;
import weka.classifiers.evaluation.Evaluation;

import java.io.IOException;
import java.util.Properties;
*/
public class MlPlanBenchmark {/* extends WekaBenchmark<WekaMLPlanWekaClassifier>{

	@Override
	protected WekaMLPlanWekaClassifier initClassifier(int timeLimit) {
		try {
			Properties mlPlanConfig = new Properties();
			mlPlanConfig.setProperty("timeout", String.valueOf(timeLimit));

			return new WekaMLPlanWekaClassifier(new MLPlanWekaBuilder()
					.withAlgorithmConfigFile(PropertiesUtils.store(mlPlanConfig, "mlplan")));
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	protected String getBestModel(WekaMLPlanWekaClassifier classifier, Evaluation eval) {
		return null;
	}

	public static void main(String[] args) {
		new MlPlanBenchmark().runClassifier(args);
	} */
}
