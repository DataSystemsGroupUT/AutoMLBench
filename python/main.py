import argparse
from os import listdir
from os.path import join
from typing import List

from benchmark import AutoSklearnBenchmark, TPOTBenchmark

import warnings
warnings.simplefilter("ignore")


models = ['autoweka', 'autosklearn', 'tpot']


def benchmark(input_dir: str, output_dir: str,
              time: int = None, n_runs: int = 5,
              split: float = 0.75, use_models: List[str] = models):

    model_to_bench = {
        'autosklearn': AutoSklearnBenchmark,
        'tpot': TPOTBenchmark,
    }
    use_models = [model_to_bench[model] for model in use_models if model in model_to_bench]

    exts = ['.csv']
    for file in listdir(input_dir):
        if any([file.endswith(ext) for ext in exts]):
            print('File: ' + file)
            dataset = join(input_dir, file)
            for model in use_models:
                print('Model: ' + model.__name__)
                model().benchmark(dataset, output_dir, time, n_runs, split)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', help='Datasets directory')
    parser.add_argument('output_dir', help='Benchmark results directory')
    parser.add_argument('-t', '--time', type=int, help='Time budget')
    parser.add_argument('-n', '--n_runs', type=int, help='Number of runs per model on dataset')
    parser.add_argument('-m', '--model', choices=models, default=models, help='AutoML Models')
    args = parser.parse_args()

    benchmark(args.input_dir, args.output_dir, args.time, args.n_runs,
              use_models=args.model if isinstance(args.model, list) else [args.model])


