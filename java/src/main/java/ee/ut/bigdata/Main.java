package ee.ut.bigdata;

import ee.ut.bigdata.impl.AutoWekaBenchmark;

import java.util.HashMap;
import java.util.Map;

public class Main {

	private static Map<String, Class<? extends Benchmark>> models = new HashMap<>();
	static {
		models.put("autoweka", AutoWekaBenchmark.class);
	}

	public static void main(String[] args) throws Exception {
		if (args.length < 4)
			throw new IllegalArgumentException("Not enough arguments. Usage: <source> <output> <timeLimit> <model>");
		String dataset = args[0];
		String output = args[1];
		int timeLimit = Integer.parseInt(args[2]);
		String model = args[3];

		Benchmark benchmark = models.get(model).newInstance();
		benchmark.benchmark(dataset, output, timeLimit, 0.75f);
	}

}
