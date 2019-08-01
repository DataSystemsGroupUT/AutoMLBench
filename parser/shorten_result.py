import pandas as pd

result = pd.read_csv(r'C:\Users\HassanEldeeb\Documents\GitHub\AutoMLBenchmarking\Logs\Results10\Results10.csv')
short_result = result.drop(['sklearn_model_1', 'sklearn_e_model_1', 'sklearn_v_model_1', 'sklearn_m_model_1', 'autoweka_model_1', 'tpot_model_1'], axis=1)
short_result.to_csv(r'C:\Users\HassanEldeeb\Documents\GitHub\AutoMLBenchmarking\Logs\Results10\Results10_short.csv')