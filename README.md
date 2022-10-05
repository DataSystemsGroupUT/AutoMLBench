# Overview:
In this study, we benchmark the most commonly used tools, i.e.AutoSKLearn,TPOT, ATM, Recipe, SmartML, AutoWeka. We analyze the underlying techniques, and experimentally study the promising areas for each tool. For instance, the effect ofmeta-learning, ensembling, time budget, search space size and robustness of the optimization process have been empiricallystudied. The statistical significance of the accuracy differenceusing these techniques has been evaluated using Wilcoxontest. The results from 100 datasets show that the ensembling mechanism generally enhance the performance accuracy while the meta-learning mechanism is effective with very short time budgets only.


### You can see a detailed results [here](https://datasystemsgrouput.github.io/AutoMLBench/)

To run the python-based framworks, please refere to the [python folder](https://github.com/DataSystemsGroupUT/AutoMLBench/blob/master/python/). Call the [main.py](https://github.com/DataSystemsGroupUT/AutoMLBench/blob/master/python/main.py), especilly the main function which has the following structure:

```python
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Dataset file')
    parser.add_argument('output_file', help='Benchmark result file')
    parser.add_argument('-t', '--time', type=int, help='Time budget')
    parser.add_argument('-m', '--model', help='AutoML Model')
    parser.add_argument('-te', '--test_file', help='Dataset test file')
    parser.add_argument('-c', '--config', nargs='*')
    args = parser.parse_args()

    benchmark(dataset_file=args.input_file, output_file=args.output_file,
              time=args.time, model=args.model, dataset_test_file=args.test_file,
              config=args.config)
```

To run the Java-based framework, namely Auto-Weka, please refere to the [Java folder](https://github.com/DataSystemsGroupUT/AutoMLBench/tree/master/java). Call the [Main.java](https://github.com/DataSystemsGroupUT/AutoMLBench/blob/master/java/src/main/java/ee/ut/bigdata/Main.java), especilly the main function which has the following structure:

```java
public class Main {

	private static Map<String, Class<? extends Benchmark>> models = new HashMap<>();
	static {
		models.put("autoweka", AutoWekaBenchmark.class);
		models.put("mlplan", MLPlanBenchmark.class);
	}

	public static void main(String[] args) throws Exception {
		if (args.length < 4)
			throw new IllegalArgumentException(
					"Not enough arguments. Usage: <model> <dataset> [<test>] <output> <timeLimit>");
		String model = args[0];
		String dataset = args[1];
		String output = args[args.length - 2];
		int timeLimit = Integer.parseInt(args[args.length - 1]);
		String test = args.length == 5? args[2]: null;

		Benchmark benchmark = models.get(model).newInstance();
		if (test == null)
			benchmark.benchmark(dataset, output, timeLimit, 0.75f);
		else {
			benchmark.benchmark(dataset, test, output, timeLimit);
		}
	}

}
```

Once all the log files are generated, we can parse them using [specific parsers](https://github.com/DataSystemsGroupUT/AutoMLBench/tree/master/parser). The output is cascaded into the this [sheet](https://github.com/DataSystemsGroupUT/AutoMLBench/blob/master/Complete_Sheet.xlsx).
