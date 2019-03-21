import argparse
import warnings
from benchmark import AutoSklearnBenchmark, TPOTBenchmark

warnings.simplefilter("ignore")


def benchmark(dataset_file: str, output_file: str,
              time: int, model: str, dataset_test_file: str = None):
    model_to_bench = {
        'autosklearn': AutoSklearnBenchmark,
        'tpot': TPOTBenchmark,
    }
    if model in model_to_bench:
        model_to_bench[model]().benchmark(dataset_file, output_file,
                                          time_limit=time, dataset_test_file=dataset_test_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Dataset file')
    parser.add_argument('output_file', help='Benchmark result file')
    parser.add_argument('-t', '--time', type=int, help='Time budget')
    parser.add_argument('-m', '--model', help='AutoML Model')
    parser.add_argument('-te', '--test_file', help='Dataset test file')
    args = parser.parse_args()

    benchmark(args.input_file, args.output_file, args.time, args.model, args.test_file)
