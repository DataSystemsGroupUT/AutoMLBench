import argparse
import json
from os import listdir
from os.path import isdir, join


def collect(output_dir: str, dataframe_dir: str):
    data = {}
    for benchmark in listdir(output_dir):
        benchmark_dir = join(output_dir, benchmark)
        if isdir(benchmark_dir):
            for dataset in listdir(benchmark_dir):
                if dataset.endswith('.json'):
                    with open(join(benchmark_dir, dataset)) as dataset_file:
                        result = json.load(dataset_file)
                        data.setdefault(benchmark, dict())[dataset] = result
    print(data)
    # TODO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output_dir', help='Benchmark results directory')
    parser.add_argument('dataframe_dir', help='Path to save dataframe')
    args = parser.parse_args()

    collect(args.output_dir, args.dataframe_dir)
