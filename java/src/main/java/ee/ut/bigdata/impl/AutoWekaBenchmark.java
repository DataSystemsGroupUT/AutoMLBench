package ee.ut.bigdata.impl;

import ee.ut.bigdata.WekaBenchmark;
import weka.classifiers.evaluation.Evaluation;
import weka.classifiers.meta.AutoWEKAClassifier;

public class AutoWekaBenchmark extends WekaBenchmark<AutoWEKAClassifier> {

	@Override
	protected AutoWEKAClassifier initClassifier(int timeLimit) {
		AutoWEKAClassifier classifier = new AutoWEKAClassifier();
		classifier.setTimeLimit(timeLimit);
		return classifier;
	}

	@Override
	protected String getBestModel(AutoWEKAClassifier classifier, Evaluation eval) {
		String[] modelOutput = classifier.toString().split("\n");
		return modelOutput[0] + "\n" + modelOutput[1];
	}

	public static void main(String[] args) {
		new AutoWekaBenchmark().runClassifier(args);
	}
}
