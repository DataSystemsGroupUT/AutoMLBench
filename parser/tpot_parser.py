import pandas as pd
import os


def parse_tpot(directory):
    result = pd.DataFrame(columns=['tpot_accuracy_1', 'tpot_f1_score_1', 'tpot_model_1',
                                   'tpot_precision_1', 'tpot_recall_1', 'tpot_time_1'])
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            sub_result = pd.read_csv(os.path.join(subdir, file), index_col='dataset')
            sub_result = sub_result[['accuracy_1', 'f1score_1', 'model_1', 'precision_1', 'recall_1', 'time_1']]
            sub_result.rename(columns={'accuracy_1': 'tpot_accuracy_1',
                                   'f1score_1': 'tpot_f1_score_1',
                                   'model_1': 'tpot_model_1',
                                   'precision_1': 'tpot_precision_1',
                                   'recall_1': 'tpot_recall_1',
                                   'time_1': 'tpot_time_1'}, inplace=True)
            result = result.append(sub_result)
    return result


def main():
    path = r'C:\Users\HassanEldeeb\Desktop\Benchmark_Deliverables\Logs\Results10\tpot'
    parse_tpot(path)


if __name__ == "__main__":
    # execute only if run as a script
    main()