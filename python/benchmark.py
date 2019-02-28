import json
import os
import time
from abc import ABC, abstractmethod
from os.path import basename, join
from utils import Thread

import pandas as pd
from autosklearn.classification import AutoSklearnClassifier
from pandas.core.dtypes.common import is_numeric_dtype
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from tpot import TPOTClassifier


class ModelBenchmark(ABC):

    @abstractmethod
    def benchmark(self, dataset_file: str, output_dir: str,
                  time_limit: int = None, n_runs: int = 5,
                  split: float = 0.75):
        '''
        Benchmark the model on a dataset and saves results to a directory
        '''
        pass

    def _output(self, dataset_file, output_dir, results = None):
        model_name = self.__class__.__name__
        dataset_name = os.path.splitext(basename(dataset_file))[0]
        if not os.path.exists(join(output_dir, model_name)):
            os.makedirs(join(output_dir, model_name))
        output_file = join(output_dir, model_name, dataset_name + '.json')
        with open(output_file, 'w') as out:
            if results is not None:
                out.write(json.dumps(results))
        return output_file


class SklearnBenchmark(ModelBenchmark, ABC):

    def benchmark(self, dataset_file: str, output_dir: str,
                  time_limit: int = None, n_runs: int = 5,
                  split: float = 0.75):
        results = []
        X, y = self._load_dataset(dataset_file)
        for _ in range(n_runs):
            X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=split)
            model = self._init_model(time_limit)

            result = {}
            time_start, time_end = time.time(), None
            try:
                train_thread = Thread(target=self._fit_model, args=(model, X_train, y_train))
                train_thread.start()
                train_thread.join(timeout=time_limit * 60 * 1.1)
                time_end = time.time()

                if train_thread.is_alive():
                    train_thread.terminate()
                    result['error'] = 'Timeout'
                else:
                    result.update(self._evaluate(model, X_test, y_test))
                    result['model'] = str(self._best_model(model))
            except Exception as e:
                result['error'] = str(e)
            finally:
                if time_end is None:
                    time_end = time.time()
                result['time'] = time_end - time_start
            results.append(result)

        self._output(dataset_file, output_dir, results)

    def _fit_model(self, model, X, y):
        model.fit(X, y)

    @abstractmethod
    def _init_model(self, time_limit: int = None):
        pass

    @abstractmethod
    def _best_model(self, model):
        pass

    def _load_dataset(self, dataset_file):
        df = pd.read_csv(dataset_file)
        X = df.drop(df.columns[-1], axis=1)
        y = df.iloc[:, -1]
        if not is_numeric_dtype(y.dtype):
            from sklearn.preprocessing import LabelEncoder
            le = LabelEncoder()
            y = le.fit_transform(y)
        return X, y

    def _evaluate(self, model, X, y):
        predictions = model.predict(X)
        return {
            'accuracy': accuracy_score(y, predictions),
            'precision': precision_score(y, predictions, average='weighted'),
            'recall': recall_score(y, predictions, average='weighted'),
            'f1score': f1_score(y, predictions, average='weighted')
        }


class AutoSklearnBenchmark(SklearnBenchmark):

    def _init_model(self, time_limit: int = None):
        return AutoSklearnClassifier(time_left_for_this_task=time if time is None else 60 * time_limit,
                                     ml_memory_limit=6144)

    def _best_model(self, model):
        return model.get_models_with_weights()


class TPOTBenchmark(SklearnBenchmark):

    def _init_model(self, time_limit: int = None):
        return TPOTClassifier(max_time_mins=time_limit)

    def _best_model(self, model):
        return model.fitted_pipeline_
