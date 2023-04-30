import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from qiskit import Aer
from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.datasets import ad_hoc_data
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit_ibm_provider import IBMProvider


class FraudDetector:
    _svm = QSVC(quantum_kernel=qkernel)

    def __init__(self, csv_path: str, used_columns: list, target_col: str):
        if len(used_columns) != 4:
            raise ValueError('The columns have to be exactly four')
        used_columns.append(target_col)

        # Load the csv file and specifying the columns
        bank_df = pd.read_csv(csv_path, usecols=used_columns)

        result_0 = bank_df.loc[bank_df[target_col] == 0]
        used_data0 = result_0.loc[:20]

        # Getting 180 fraud records
        result_1 = bank_df.loc[bank_df[target_col] == 1]
        result_1 = result_1.reset_index()
        used_data1 = result_1.loc[:180]

        # Joining the records
        frames = [used_data0, used_data1]
        result = pd.concat(frames)
        result = result.reset_index()

        # Converting the records to integer type
        result = result.astype(int)

        # Setting up the quantum Backend
        provider = IBMProvider(instance='ibm-q-startup/qbraid/main')
        backend = provider.get_backend('ibmq_qasm_simulator')

        # Dataframe for all the labels excepts for the fraud marking
        X = result.iloc[:, :-1]

        # Dataframe for the fraud marking
        y = result.iloc[:, -1]

        # Splitting the data tow parts 70% for training and the rest for measuring the accuracy
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Encode the training and testing data onto a quantum circuit using the ZZFeatureMap
        feature_map = ZZFeatureMap(X.shape[1], reps=2)
        qkernel = QuantumKernel(feature_map, quantum_instance=backend)
        # self._svm = QSVC(quantum_kernel=qkernel)

        # Train the QSVC algorithm on the training data
        self._svm.fit(X_train, y_train)

        # Test the QSVC algorithm on the testing data
        y_pred = self._svm.predict(X_test)

        # Calculating the accuracy
        self._accuracy = np.mean(y_pred == y_test)
        print("Accuracy:", self._accuracy)

    def getAccuracy(self):
        return self._accuracy

    def predictFraud(self, features: list):
        if len(features) != 4:
            raise ValueError('The columns have to be exactly four')
        return self.predict(features)

    def getPrediction(self, features: list):
        if self.predictFraud(features=features):
            return "Fraud"
        return "Not Fraud"

