package ee.ut.bigdata;

import ee.ut.bigdata.impl.AutoWekaBenchmark;

import java.io.File;
import java.util.HashMap;
import java.util.Map;

public class Main {

	private static Map<String, Class<? extends Benchmark>> models = new HashMap<>();
	static {
		models.put("autoweka", AutoWekaBenchmark.class);
	}

	public static void main(String[] args) throws Exception {
		if (args.length < 4)
			throw new IllegalArgumentException("Not enough arguments. Usage: <source> <output> <timeLimit> <nRuns>");
		String source = args[0];
		String output = args[1];
		int timeLimit = Integer.parseInt(args[2]);
		int nRuns = Integer.parseInt(args[3]);
		float split = 0.75f;

		File path = new File(source);
		for (File file: path.listFiles()){
			if (file.isFile() && file.getName().endsWith(".csv")){
				System.out.println("File: " + file.getName());
				for (Class<? extends Benchmark> benchmarkClass: models.values()) {
					System.out.println("Model: " + benchmarkClass.getSimpleName());
					benchmarkClass.newInstance().benchmark(file.getAbsolutePath(), output,
							timeLimit, nRuns, split);
				}
			}
		}
	}

}
