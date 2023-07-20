
from pathlib import Path

from datetime import datetime
from pathlib import Path
class A:
    def write_to_log_file(self,path1,path2):
        message1="this is first msg \n"
        message2="this is sec msg "
        file1= open(path1,'w')
        file1_content=file1.write(message1)
        file2=open(path2,'w')
        file2_content=file2.write(message2)
        file1.close()
        file2.close()
        f1=open(path1,'r')
        f2=open(path2,'r')
        print(f1.read())
        f1.close()
        f2.close()
        first=open(path1,'a+')
        second=open(path2,'r')
        first.write(second.read())
        first.seek(0)
        second.seek(0)
        # f1=open(file1,'a+')
        # f2=open(file2,'r')
        # f1.write(f2.read())
path1='C:/Users/vgunaganti/PycharmProjects/HelloWorld/file1.txt'
path2='C:/Users/vgunaganti/PycharmProjects/HelloWorld/file2.txt'
obj=A()
obj.write_to_log_file(path1,path2)