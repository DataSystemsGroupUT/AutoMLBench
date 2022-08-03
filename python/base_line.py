import pandas as pd
import numpy as np
import glob
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings("ignore")

#Intialise a random number generator
rng = np.random.default_rng(0)



path = "./Datasets/*train.csv"
# df_result = pd.DataFrame(columns=['ds_name', 'acc'])
df_result = pd.read_csv('base_line_results.csv', index_col=False)
for fname_tr in glob.glob(path):
    if (df_result['ds_name'].eq(fname_tr.rsplit('_', 1)[0])).any():
        continue
    print(fname_tr)
    fname_ts = fname_tr.rsplit('_', 1)[0] + '_test.csv'
    df_tr = pd.read_csv(fname_tr, na_values='?')
    df_ts = pd.read_csv(fname_ts, na_values='?')

    df_tr = df_tr.fillna(9999)
    df_ts = df_ts.fillna(9999)

    data = pd.concat([df_tr, df_ts])
    categorical_ = data.select_dtypes(['object']).columns
    lab_encs = {col: LabelEncoder().fit(data[col].astype('str')) for col in categorical_}

    for col in categorical_:
        df_tr[col] = lab_encs[col].transform(df_tr[col].astype('str'))
        df_ts[col] = lab_encs[col].transform(df_ts[col].astype('str'))

    y_col = df_tr.columns[-1]
    x_tr, y_tr, x_ts, y_ts = df_tr.drop(y_col, axis=1), df_tr[y_col], df_ts.drop(y_col, axis=1), df_ts[y_col]
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(x_tr, y_tr)
    y_prid = clf.predict(x_ts)
    acc = accuracy_score(y_ts, y_prid)
    df_result = df_result.append({'ds_name': fname_tr.rsplit('_', 1)[0], 'acc': acc}, ignore_index = True)
    
    df_result.to_csv('base_line_results.csv', index=False)

