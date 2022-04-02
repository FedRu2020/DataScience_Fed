#!/usr/bin/env python
# coding: utf-8

# #### Импорт всех нужных библиотек

# In[1]:


import numpy as np 
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import joblib
from boxkite.monitoring.service import ModelMonitoringService


def main():
    dataset = pd.read_csv('winequality-red.csv', sep=";")
    #  выделим названия числовых колонок кроме целевой переменной 
    num_cols = [i for i in dataset.columns if dataset[i].dtype =='float64']
    
    dataset['Bi_qlt'] = dataset['quality'].apply(lambda x: 'bad wine' if x<6.5 else 'good wine')

    X_cat = OneHotEncoder(sparse = False).fit_transform(dataset[['Bi_qlt']])
    X_num = StandardScaler().fit_transform(dataset[num_cols].values)
    X = np.hstack([X_num, X_cat])
    y = dataset.quality
    
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.2)


    clf = SVC(C=100, gamma=0.01, kernel='rbf', probability=True)

    model = clf.fit(train_X, train_y)
    pred_y = model.predict(test_X)


    dict_rep = classification_report(test_y, pred_y, zero_division=1, output_dict=True)
    f1_score = round(dict_rep['weighted avg']['f1-score'],3)
    precision = round(dict_rep['weighted avg']['precision'],3)
    recall_score = round(dict_rep['weighted avg']['recall'],3)
    accuracy = round(dict_rep['accuracy'],3)

    print(f'F1 score: {f1_score}')
    print('------------------------------------------')
    print(f'Precision: {precision}')
    print('------------------------------------------')
    print(f'Recall: {recall_score}')
    print('------------------------------------------')
    print(f'accuracy: {accuracy}')


    # Запись в пикл
    joblib.dump(model, 'Rwine_model.pkl')
    model = joblib.load('Rwine_model.pkl')
    
    features = zip(*[dataset.columns[:-2], train_X.T])
    ModelMonitoringService.export_text(features=features, path="./histogram.prom",)


if __name__=="__main__":
    main()

