import PIL.Image as Image
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from pca import *
from sklearn import datasets 


# knn输入是ndarray类型,标签是list类型
# 神经网络内部要比较简单,数据量少,防止过拟合
# 可以尝试迁移学习等等



def pre_knn():
    t1=MyPca("D:\\study\\pattern_recognition\\数据集\\数据集\\train")
    x_train=t1.my_pca()
    print(x_train.size)
    # x_train=x_train.tolist()
    y_train=[]
    file_list=os.listdir("D:\\study\\pattern_recognition\\数据集\\数据集\\train")
    for fi in file_list:
        # print(fi.split("_")[0])
        y_train.append(fi.split("_")[0])
        pass
    print(len(y_train))
    t2=MyPca("D:\\study\\pattern_recognition\\数据集\\数据集\\test_all3")
    x_test=t2.my_pca()
    # print(x_test.size)
    # x_train=x_train.tolist()
    y_test=[]
    file_list=os.listdir("D:\\study\\pattern_recognition\\数据集\\数据集\\test_all3")
    for fi in file_list:
        # print(fi[0])
        y_test.append(fi.split("_")[0])
        pass
    # print(len(y_test))
    return x_train,y_train,x_test,y_test
    pass



if __name__=="__main__":
    # iris = datasets.load_iris()
    # print(type(iris.data))
    x_train,y_train,x_test,y_test=pre_knn()
    # print(x_train.size)
    # print(len(y_train))
    # print(x_test.size)
    # print(len(y_test))

    knn = KNeighborsClassifier(n_neighbors=10,algorithm='auto')    #实例化KNN模型
    knn.fit(x_train, y_train)      #放入训练数据进行训练
    print(knn.predict(x_test))           #打印预测内容
    print(y_test)     #实际标签
    score=knn.score(x_test,y_test,sample_weight=None)
    print(score)
    pass