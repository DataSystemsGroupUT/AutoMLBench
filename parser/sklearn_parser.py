import pandas as pd
import os


def parse_sklearn_v(directory):
    result = pd.DataFrame(columns=['sklearn_v_accuracy_1', 'sklearn_v_f1_score_1', 'sklearn_v_model_1',
                           'sklearn_v_precision_1', 'sklearn_v_recall_1', 'sklearn_v_time_1'])
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            sub_result = pd.read_csv(os.path.join(directory, file), index_col='dataset')
            sub_result = sub_result[['accuracy_1', 'f1score_1', 'model_1', 'precision_1', 'recall_1', 'time_1']]
            sub_result.rename(columns={'accuracy_1': 'sklearn_v_accuracy_1',
                                   'f1score_1': 'sklearn_v_f1_score_1',
                                   'model_1': 'sklearn_v_model_1',
                                   'precision_1': 'sklearn_v_precision_1',
                                   'recall_1': 'sklearn_v_recall_1',
                                   'time_1': 'sklearn_v_time_1'}, inplace=True)
            result = result.append(sub_result)
    return result


def parse_sklearn_m(directory):
    result = pd.DataFrame(columns=['sklearn_m_accuracy_1', 'sklearn_m_f1_score_1', 'sklearn_m_model_1',
                                   'sklearn_m_precision_1', 'sklearn_m_recall_1', 'sklearn_m_time_1'])
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            sub_result = pd.read_csv(os.path.join(directory, file), index_col='dataset')
            sub_result = sub_result[['accuracy_1', 'f1score_1', 'model_1', 'precision_1', 'recall_1', 'time_1']]
            sub_result.rename(columns={'accuracy_1': 'sklearn_m_accuracy_1',
                                   'f1score_1': 'sklearn_m_f1_score_1',
                                   'model_1': 'sklearn_m_model_1',
                                   'precision_1': 'sklearn_m_precision_1',
                                   'recall_1': 'sklearn_m_recall_1',
                                   'time_1': 'sklearn_m_time_1'}, inplace=True)
            result = result.append(sub_result)
    return result


def parse_sklearn_e(directory):
    result = pd.DataFrame(columns=['sklearn_e_accuracy_1', 'sklearn_e_f1_score_1', 'sklearn_e_model_1',
                                   'sklearn_e_precision_1', 'sklearn_e_recall_1', 'sklearn_e_time_1'])
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            sub_result = pd.read_csv(os.path.join(directory, file), index_col='dataset')
            sub_result = sub_result[['accuracy_1', 'f1score_1', 'model_1', 'precision_1', 'recall_1', 'time_1']]
            sub_result.rename(columns={'accuracy_1': 'sklearn_e_accuracy_1',
                                   'f1score_1': 'sklearn_e_f1_score_1',
                                   'model_1': 'sklearn_e_model_1',
                                   'precision_1': 'sklearn_e_precision_1',
                                   'recall_1': 'sklearn_e_recall_1',
                                   'time_1': 'sklearn_e_time_1'}, inplace=True)
            result = result.append(sub_result)
    return result


def parse_sklearn(directory):
    result = pd.DataFrame(columns=['sklearn_accuracy_1', 'sklearn_f1_score_1', 'sklearn_model_1',
                                   'sklearn_precision_1', 'sklearn_recall_1', 'sklearn_time_1'])
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            sub_result = pd.read_csv(os.path.join(directory, file), index_col='dataset')
            sub_result = sub_result[['accuracy_1', 'f1score_1', 'model_1', 'precision_1', 'recall_1', 'time_1']]
            sub_result.rename(columns={'accuracy_1': 'sklearn_accuracy_1',
                                   'f1score_1': 'sklearn_f1_score_1',
                                   'model_1': 'sklearn_model_1',
                                   'precision_1': 'sklearn_precision_1',
                                   'recall_1': 'sklearn_recall_1',
                                   'time_1': 'sklearn_time_1'}, inplace=True)
            result = result.append(sub_result)
    return result


def main():
    path = r'C:\Users\HassanEldeeb\Desktop\Benchmark_Deliverables\Logs\Results10\autosklearn'
    parse_sklearn(path)


if __name__ == "__main__":
    # execute only if run as a script
    main()