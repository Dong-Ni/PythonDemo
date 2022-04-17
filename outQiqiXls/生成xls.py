#推荐使用pandas，使用pandas方法可以不用在excel上点击
import pandas as pd
import numpy as np
import os
# 
os.getcwd() 
#获取当前路径
def get_img_file(file_dir):
        imagelist = []
        for parent, dirnames, filenames in os.walk(file_dir):
            #print('parent === ')
            #print(parent)
            #print('dirnames  === ')
            #print(dirnames)
            #print('filenames  === ')
            #print(filenames)
            for dirname in dirnames:
                        # 判断文件是否是图片形式，这里的后缀名都是默认小写字母形式，如有大写字母，添加上去即可
                        #print(filename)
                imagelist.append(os.path.join(parent, dirname))
                        #print(filename)
        return imagelist

def get_img_name(file_dir):
        imagelist = []
        for parent, dirnames, filenames in os.walk(file_dir):
            #print('parent === ')
            #print(parent)
            #print('dirnames  === ')
            #print(dirnames)
            #print('filenames  === ')
            #print(filenames)
            for dirname in dirnames:
                imagelist.append(dirname)
                        #print(filename)
        return imagelist

def Hyperlinks(data_list,file_paths):
        str_1= '=HYPERLINK("'
        str_2 = '","'
        str_3 = '")'
        list_ = []
        for i,j in zip(data_list,file_paths):
                list_.append(str_1 + j + str_2 + str(i) + str_3)
        return list_

def get_current_dir(filepath):
        dirpath = []
        for f in os.listdir(filepath):
                absolute_path = os.path.join(filepath, f)
                if os.path.isdir(absolute_path):
                        dirpath.append(absolute_path)
        return dirpath
                        

if __name__ == "__main__":
    #file_dir = os.getcwd()
    file_dir = '.\\'
    dirpath = get_current_dir(file_dir)
    print("dirpath = ", dirpath)
    
    #print("tmppath = ", tmppath)
    #file_dir = 'D:\\2021-12'
    imagelist = get_img_file(file_dir) #获取指定文件夹下的存放路径以及名称
    print("imagelist = ", imagelist)
    listlen = len(imagelist)
    data = np.arange(0, listlen)
    print(data)
    imagename = get_img_name(file_dir)
    print("imagename = ", imagename)

    #生成excel
    data_df  = pd.DataFrame(imagename)
    data_df.columns = ['test']
    print("data_df  = ", data_df)
    #dstTmp = file_dir + '\\newTmp.xlsx'
    #writer = pd.ExcelWriter(dstTmp)
    #data_df.to_excel(writer,float_format='%.5f')
    #writer.save()

    #dataxls = pd.read_excel(dstTmp) #导入数据
    #print("dataxls =", dataxls)
    data_list = data_df['test'] #设置需要生成超链接的列
    print('data_list =', data_list)
    test_list = Hyperlinks(data_list,imagelist) #调用Hyperlinks
    print("test_list = ", test_list)
    data_df['test'] = test_list
    dsttarget = file_dir + '\\new_qiqi.xlsx'
    data_df.to_excel(dsttarget,index=False)
    #os.remove(dstTmp)
    print('文件成功生成')
