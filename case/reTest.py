#encoding:utf-8
#@Time:2020/1/16 9:58
#@Author:sunny

import re
t="255.254.253.110"
t1=re.compile(r'(\d+\.){0}')
t2=re.compile(r'(\d+\.){1}\d+')
t3=re.compile(r'(\d+\.){2}\d+')
t4=re.compile(r'(\d+\.){3}\d+')
t5=re.compile(r'(\d+\.){4}\d+')

print(t1.findall(t))
print(t2.findall(t))
print(t3.findall(t))
print(t4.findall(t))
print(t5.findall(t))
