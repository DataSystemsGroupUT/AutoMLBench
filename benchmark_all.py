import argparse
import os
import subprocess

autoweka_benchmark_jar = 'java/automl-benchmarking-0.0.1-SNAPSHOT-jar-with-dependencies.jar'
# Set path to autoweka.jar #
autoweka_jar = '/home/olehmatsuk/autoweka-2.6/autoweka.jar'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', help='Datasets directory')
    parser.add_argument('result_dir', help='Benchmark results directory')
    parser.add_argument('-t', '--time', type=int, help='Time budget')
    parser.add_argument('-n', '--n_runs', type=int, help='Number of runs per model on dataset')
    args = parser.parse_args()
    tmp_output = 'tmp'

    # Python tool benchmarks
    subprocess.run('python python/main.py {} {} -t {} -n {}'
                   .format(args.input_dir, tmp_output, args.time, args.n_runs), shell = True)

    # Java tool benchmarks
    jars = autoweka_benchmark_jar + ':' + autoweka_jar
    subprocess.run('java -cp "{}" ee.ut.bigdata.Main {} {} {} {}'
                   .format(jars, args.input_dir, tmp_output, args.time, args.n_runs), shell = True)

    # collect results
    subprocess.run('python python/collect.py {} {}'
                   .format(tmp_output, args.result_dir), shell=True)

