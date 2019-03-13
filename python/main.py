import argparse
import warnings
from benchmark import AutoSklearnBenchmark, TPOTBenchmark

warnings.simplefilter("ignore")


def benchmark(dataset_file: str, output_file: str,
              time: int, model: str, split: float = 0.75):
    model_to_bench = {
        'autosklearn': AutoSklearnBenchmark,
        'tpot': TPOTBenchmark,
    }
    model_to_bench[model]().benchmark(dataset_file, output_file, time, split)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Datasets directory')
    parser.add_argument('output_file', help='Benchmark results directory')
    parser.add_argument('-t', '--time', type=int, help='Time budget')
    parser.add_argument('-m', '--model', help='AutoML Models')
    args = parser.parse_args()

    benchmark(args.input_file, args.output_file, args.time, args.model)
