#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from numpy import equal

def write_index(path, num):
    if os.path.basename(path)[0] == '.' and len(os.path.basename(path)) > 1:
        return

    num = num + 1
    allfilelist=os.listdir(path)
    for f in allfilelist:
        tempf = os.path.join(path, f)
        #判断是不是文件夹
        if os.path.isdir(tempf):
            if (f == ".git") or f == "code":
                continue
            temp = "\n"
            for n in range(num):
                temp = temp + "#"
            temp = temp + " " + os.path.basename(tempf) + "\n"
            if (f != "." and f != ".." and num < 4) :
                file.write(temp)
            write_index(tempf, num)
        elif tempf.endswith(".md"): 
            temp = "- " + "[" + os.path.basename(tempf).split('.')[0] + "]" + "(" + tempf + ")" + "\n"
            temp = temp.replace("\\", "/")
            file.write(temp)

filepath = "readme.md"
# 判断文件是否存在
if (os.path.exists(filepath)) :
	#存在，则删除文件
	os.remove(filepath)

file = open(filepath,'a',encoding="UTF-8")
file.write("# easy blog\n")
write_index(".", 1)
file.close()