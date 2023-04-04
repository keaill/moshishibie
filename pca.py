import PIL.Image as Image
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.model_selection import cross_val_score




# 不用rgb，直接灰值就可以，色彩不会影响模式识别，这是人为的特征提取
# 还没用pca之前，先完成一次特征提取
# 如果用上rgb，可能会是不必要的拖累
# 图片生成方式需要一样吗，例如不要留太多空白？图片大小应该一致？
# 数据大小不一样如何用pca？转换？
# pca是无监督学习算法
# pca是对属性维度进行降维,而图片个数是不能改变的,我们先将属性融合,然后用图片中最有用的新属性来代表图片,而图片个数不变
# 对于cnn来说,cnn是处理空间特性的,正常情况下输入应该是一个二维矩阵,我们先用pca降维,将二维矩阵转换成一维向量,例如一维向量为1600,降维后为100,我们需要再将一维向量转换成10×10的二维矩阵,用于cnn
# cnn是处理空间特性,而不仅仅是图片,因此我们只需要一个空间结构进去,这相当于在cnn之前先用pca进行一次特征提取.








class MyPca:        
    def __init__(self,file_list_path):
        self.pre_pca_list=[]
        # 文件夹路径
        self.file_list_path = file_list_path
        self.width=50
        self.height=50
        pass
    # 对一张图片
    def pic2num(self):
        # 读取图片
        image = Image.open(self.file_path)
        # 显示图片
        # image.show()
        # 调整大小
        img_size=image.resize((self.width,self.height))
        img_size.save(self.file_path,'BMP')
        image.close()

        image = Image.open(self.file_path)
        width, height = image.size
        # 灰度化
        image_grey = image.convert("L")
        data = image_grey.getdata()
        # 化成矩阵
        data = np.array(data, dtype="float") / 255.0
        new_data = np.reshape(data, (1, height*width))
        # print(new_data)#ndarray
        # print(new_data.shape)
        # 矩阵变数组，数组变列表
        # new_data=new_data.A
        # new_data=new_data.tolist()
        # print(new_data)
        self.pre_pca_list.append(new_data[0])
        # print(self.pre_pca_list)
        image.close()
    # 对整个数据集
    def get_all_data(self):
        file_list=os.listdir(self.file_list_path)
        for fi in file_list:
            self.file_path=self.file_list_path+"\\"+fi
            # print(self.file_path)
            self.pic2num()
            # print(fi)
            pass
        # print(len(self.pre_pca_list[1]))
        # print(self.pre_pca_list)
        self.a=np.array(self.pre_pca_list,dtype=np.float32)
        # print(self.a[0][22])
    def my_pca(self):   
        self.get_all_data()
        pca = PCA(n_components=100)
        newX = pca.fit_transform(self.a)     #等价于pca.fit(X) pca.transform(X)
        # newX=newX.tolist() 
        # print(newX[0])
        # invX = pca.inverse_transform(newX)
        print(pca.explained_variance_ratio_.sum())
        print(type(newX))#ndarray
        print(newX.size)

        # score = []
        # for i in range(60, 100):
        #     pca = PCA(n_components=i)
        #     newX = pca.fit_transform(self.a)  #等价于pca.fit(X) pca.transform(X)
        #     one_score = pca.explained_variance_ratio_.sum()
        #     score.append(one_score)
        # plt.plot(range(60, 100), score)
        # # plt.savefig(r"C:\Users\86377\Desktop\3.png")
        # plt.show()
        return newX
        pass



if __name__=="__main__":
    t=MyPca("D:\\study\\pattern_recognition\\数据集\\数据集\\train")
    t.get_all_data()
    # t.pic2num()


# 链接
# 图像转换:
# https://blog.csdn.net/wzk4869/article/details/126083092?utm_source=app&app_version=5.5.0&code=app_1562916241&uLinkId=usr1mkqgl919blen
# https://blog.csdn.net/qq_28626909/article/details/89365107?utm_source=app&app_version=5.5.0&code=app_1562916241&uLinkId=usr1mkqgl919blen
# pca
# https://blog.csdn.net/qq_20135597/article/details/95247381
# https://blog.csdn.net/baidu_41797613/article/details/121844644
# https://blog.csdn.net/m0_45184077/article/details/114639115  对于pca的图像分析
# https://blog.csdn.net/qq_36895331/article/details/117221237

    
