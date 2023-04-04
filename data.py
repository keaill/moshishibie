# coding=utf-8
 
import os
import re

target=['ha','er','bin','gong','ye','da','xue','de','xiao','xun','shi','gui','ge','yan','ge','gong2','fu','dao','jia']
a=[]
for i in range(19):
    a.append(0)
a[14]=900

def rename(path,path2):
    file_list=os.listdir(path)
    i=0
   
    for fi in file_list:
        p1=fi.find("_",0,len(fi))  
        p2=fi.find(".",0,len(fi))
        i=fi[p1+1:p2]
        i=int(i)-1
        # if(i%19==0): 
        #     j=j+1
        # if(i%19==14):
        #     z=900+j
        # if(i%19==14):
        #     t=z  
        # else:
        #     t=j
        
        path_result=path+"\\"+fi
        f1=open(path_result,"rb")
        data=f1.read()
        f1.close()
        
        temp=i%19
        a[temp]=a[temp]+1
        new_name=str(target[temp])+'_'+str(a[temp])+"_s"
        with open(path2+'\\'+new_name+'.bmp', 'wb') as f:
            # with open('./results'+name+'.jpg', 'wb+') as f:
            f.write(data)
            f.close()
        # os.rename(old_name,new_name)
        


if __name__=="__main__":
    path="D:\\study\\pattern_recognition\\数据集\\数据集\\train_small"
    path2="D:\\study\\pattern_recognition\\数据集\\数据集\\train_small3"
    rename(path,path2)
