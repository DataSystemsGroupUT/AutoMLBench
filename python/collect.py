import argparse
import json
from os import listdir, makedirs
from os.path import isdir, join, exists

import pandas as pd


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

    if not exists(dataframe_dir):
        makedirs(dataframe_dir)

    for benchmark, datasets in data.items():
        benchmark_data = {}
        for dataset, runs in datasets.items():
            dataset_data = {}
            run_values = {}
            for i, run in enumerate(runs):
                for k, v in run.items():
                    dataset_data['{}_{}'.format(k, i + 1)] = v

                    if k not in ['error', 'model']:
                        run_values.setdefault(k, []).append(v)
            for k, vs in run_values.items():
                dataset_data[k] = sum(vs) / len(vs)
            benchmark_data[dataset] = dataset_data
        df = pd.DataFrame.from_dict(benchmark_data, orient='index')
        df.to_csv(join(dataframe_dir, benchmark + '.csv'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output_dir', help='Benchmark results directory')
    parser.add_argument('dataframe_dir', help='Path to save dataframe')
    args = parser.parse_args()

    collect(args.output_dir, args.dataframe_dir)
