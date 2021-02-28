import os
import shutil

#os.makedir(C:/Users/prade/Desktop/python/txt)
#source=(C:/Users/prade/Desktop/python/text.txt)
#destination=(C:/Users/prade/Desktop/python/txt)
#a=shutil.move(source,destination)
#
#src=(C:/Users/prade/Desktop/python/photo)

path=input("Enter the path")
files=os.listdir(path)
print(files)
for file in files:
        name,ext=os.path.splitext(file)
        print(name)
        print(ext)
        ext=ext[1:]
        if ext=="":
                continue
        if os.path.exists(path+'/'+ext):
                shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
        else:
                os.makedirs(path+'/'+ext)
                shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
