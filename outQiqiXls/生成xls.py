#推荐使用pandas，使用pandas方法可以不用在excel上点击
import pandas as pd
import numpy as np
import os
# 
os.getcwd() 
#获取当前路径下文件夹路径
def get_current_dir(filepath):
        dirpath = []
        for f in os.listdir(filepath):
                absolute_path = os.path.join(filepath, f)
                if os.path.isdir(absolute_path):
                        dirpath.append(absolute_path)
        return dirpath

#获取当前路径下文件夹名称
def get_current_dir_name(filepath):
        dirpathname = []
        for f in os.listdir(filepath):
                print("f = ", f)
                absolute_path = os.path.join(filepath, f)
                print("f = ", f)
                if os.path.isdir(absolute_path):
                        dirpathname.append(f)
        return dirpathname

#生成超链接
def Hyperlinks(data_list,file_paths):
        str_1= '=HYPERLINK("'
        str_2 = '","'
        str_3 = '")'
        list_ = []
        for i,j in zip(data_list,file_paths):
                list_.append(str_1 + j + str_2 + str(i) + str_3)
        return list_

if __name__ == "__main__":
    file_dir = '.\\'
    
    dirpath = get_current_dir(file_dir)
    print("dirpath = ", dirpath)
    dirname = get_current_dir_name(file_dir)
    print("dirname = ", dirname)


    #生成excel
    data_df  = pd.DataFrame(dirname)
    data_df.columns = ['test']
    print("data_df  = ", data_df)

    data_list = data_df['test'] #设置需要生成超链接的列
    print('data_list =', data_list)
    test_list = Hyperlinks(data_list,dirpath) #调用Hyperlinks
    print("test_list = ", test_list)
    data_df['test'] = test_list
    dsttarget = file_dir + '\\new_qiqi.xlsx'
    data_df.to_excel(dsttarget,index=False)
    
    print('文件成功生成')
