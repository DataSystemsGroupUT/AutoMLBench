package ee.ut.bigdata;

public interface Benchmark {

	/**
	 * Benchmark the model on a dataset and saves results to a directory
	 */
	void benchmark(String dataset, String output, int timeLimit, int nRuns, float split);

}
