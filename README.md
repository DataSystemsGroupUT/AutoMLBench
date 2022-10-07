# Overview:
In this study, we benchmark the most commonly used tools, i.e., AutoSKLearn,TPOT, ATM, Recipe, SmartML, and AutoWeka. We analyze the underlying techniques and experimentally study the promising areas for each tool. For instance, the effect of meta-learning, ensembling, time budget, search space size and robustness of the optimization process have been empirically studied. The statistical significance of the accuracy differenceusing these techniques has been evaluated using Wilcoxon test. The results from 100 datasets show that the ensembling mechanism generally enhances the performance accuracy while the meta-learning mechanism is effective with very short time budgets only.


### You can see a detailed results [here](https://datasystemsgrouput.github.io/AutoMLBench/)

### Python-based Frameworks
To run the python-based frameworks, please refer to the [python folder](https://github.com/DataSystemsGroupUT/AutoMLBench/blob/master/python/). Call the [main.py](https://github.com/DataSystemsGroupUT/AutoMLBench/blob/master/python/main.py), especially the main function, which has the following structure:

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

### Auto-Weka

To run the Java-based framework, Auto-Weka, please refer to the [Java folder](https://github.com/DataSystemsGroupUT/AutoMLBench/tree/master/java). Call the [Main.java](https://github.com/DataSystemsGroupUT/AutoMLBench/blob/master/java/src/main/java/ee/ut/bigdata/Main.java), especially the main function, which has the following structure:

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

Once all the log files are generated, we can parse them using [specific parsers](https://github.com/DataSystemsGroupUT/AutoMLBench/tree/master/parser). The output is cascaded into this [sheet](https://github.com/DataSystemsGroupUT/AutoMLBench/blob/master/Complete_Sheet.xlsx).

### Smart-ML
To run the R-based framework on the benchmarking datasets, Smart-ML, please refer to the [SmartML Repo](https://github.com/DataSystemsGroupUT/SmartML). Call the the following code snippet to run the benchmark using SmartML:

```R
install_github("DataSystemsGroupUT/SmartML")
```

```R
library(SmartML)
library(tictoc)
#################################################################################################
seeds <- c(1, 2, 3) # Setting the random seeds
nModelsAll <- c(1, 5) # Size of the output ensemble model - Running without ensemble and with ensemble of size 5
path_to_csv <- "~/all" # Path to the folder containing the datasets
files<-list.files(path_to_csv, pattern = "\\.csv$")
for(k in 1:3){
  time_budget = 60 * 1 # Time budget in minutes
  nModels = 5
  for(e in c(3)){
    for(i in seq(from=1, to=length(files), by=2)) {
      train_file = paste0(path_to_csv, "/", files[i+1])
      test_file = paste0(path_to_csv, "/", files[i])
      print(train_file)
      print(test_file)
      # Read and Preprocess Datasets
      results <- autoRLearn(time_budget, train_file, test_file, nModels=nModels, ensemble=e, seed=seeds[k]) # the main entry point to run SmartML
      print(results)
      
      # Save results
      results$model = NULL # Remove the fitted model
      results$pred = NULL # Remove predictions on the test split
      results$ensemble = e
      results$time = time_budget
      results$dataset = train_file
      results$params = paste(results$params, collapse='#')
      write.table(results, file="results_60.csv", append = T, sep=',', row.names=F, col.names=F) # Saving the results to a csv file
      gc()
    }
  }
}
```

The output CSV file will have the results in the same following order:
```
Selected Model, Selected Hyper-parameters, Test-Set Performance, ensemble size, time budget, dataset path
```

You can customize the parameters used in SmartML execution through the following:
```R
""""""
argument maxTime Float numeric of the maximum time budget for reading dataset, preprocessing, calculating meta-features, Algorithm Selection & hyper-parameter tuning process only in minutes(Excluding Model Interpretability) - This is applicable in case of Option = 2 only.
argument directory String Character of the training dataset directory (SmartML accepts file formats arff/(csv with columns headers) ).
argument testDirectory String Character of the testing dataset directory (SmartML accepts file formats arff/(csv with columns headers) ).
argument classCol String Character of the name of the class label column in the dataset (default = 'class').
argument vRatio Float numeric of the validation set ratio that should be splitted out of the training set for the evaluation process (default = 0.1 --> 10%).
argument preProcessF vector of string Character containing the name of the preprocessing algorithms (default = c('standardize', 'zv') --> no preprocessing):
supported values:
boxcox: apply a Box–Cox transform and values must be non-zero and positive in all features,
yeo-Johnson: apply a Yeo-Johnson transform, like a BoxCox, but values can be negative,
zv: remove attributes with a zero variance (all the same value),
center: subtract mean from values,
scale: divide values by standard deviation,
standardize: perform both centering and scaling,
normalize: normalize values,
pca: transform data to the principal components,
ica: transform data to the independent components.
argument featuresToPreProcess Vector of number of features to perform the feature preprocessing on - In case of empty vector, this means to include all features in the dataset file (default = c()) - This vector should be a subset of code{selectedFeats}.
argument nComp Integer numeric of Number of components needed if eitherpca" orica" feature preprocessors are needed.
argument nModels Integer numeric representing the number of classifier algorithms that you want to select based on Meta-Learning and start to tune using Bayesian Optimization (default = 5).
argument option Integer numeric representing either Classifier Algorithm Selection is needed only = 1 or Algorithm selection with its parameter tuning is required = 2 which is the default value.
argument featureTypes Vector of either 'numerical' or 'categorical' representing the types of features in the dataset (default = c() --> any factor or character features will be considered as categorical otherwise numerical).
argument interp Boolean representing if model interpretability (Feature Importance and Interaction) is needed or not (default = FALSE) This option will take more time budget if set to 1.
argument missingOpr Boolean variable represents either use median/mode imputation for instances with missing values (FALSE) or apply imputation usingMICE library which helps you imputing missing values with plausible data values that are drawn from a distribution specifically designed for each missing datapoint (TRUE).
argument balance Boolean variable represents if SMOTE class balancing is required or not (default FALSE).
argument metric Metric of string character to be used in evaluation:
supported values:
acc: Accuracy,
avg-fscore: Average of F-Score of each label,
avg-recall: Average of Recall of each label,
avg-precision: Average of Precision of each label,
fscore: Micro-Average of F-Score of each label,
recall: Micro-Average of Recall of each label,
precision: Micro-Average of Precision of each label.
"""
autoRLearn <- function(maxTime, directory, testDirectory, classCol = 'class', metric = 'acc',
                       vRatio = 0.333, preProcessF = c('standardize', 'zv'), ensemble = 1,
                       featuresToPreProcess = c(), nComp = NA, nModels = 5, option = 2,
                       featureTypes = c(), interp = FALSE, missingOpr = FALSE, balance = FALSE, seed=22)
```

