import os
import shutil

filenames = set()
def Copy(namedir,filelist):
    for curpath in filelist:# Проход по всему содержимому дирректории
        dist = os.path.join(namedir,curpath)# Полный путь для элемента дирректории
        tmp = os.path.splitext(curpath);
        if (len(tmp) == 2 and (tmp[1] == ".txt" or tmp[1] == ".TXT")):
            filename = tmp[0]
            if filename in filenames:
                i = 1
                while filename+str(i) in filenames:
                    i+=1
                filename+=str(i)
            filenames.add(filename)
            shutil.copy(dist,os.path.join(out,filename+'.txt'))
        elif os.path.isdir(dist):
            second_filelist = os.listdir(dist)
            Copy(dist,second_filelist)#Рекурсивный вызов функции для вложенных дирректорий

inp = os.path.abspath(raw_input("Enter Input Directory\n"))
out = os.path.abspath(raw_input("Enter Output Directory\n"))

if inp == out:
    print "input and output directories is equal"
else:
     if os.path.exists(inp):
         filelist = []
         try:
             if not os.path.exists(out):
                 os.mkdir(out)
             filelist = os.listdir(inp)
             Copy(inp,filelist)
             print "COMPLETE!"
         except WindowsError as e:
             print "INCORRECT PATH: "+out
     else:
         print inp+" is not exists"
