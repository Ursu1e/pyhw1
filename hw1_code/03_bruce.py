import os
import time as time
import numpy as np
def read_file(file_name):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    f_name = os.path.join(dir_name,file_name)
    l = list()
    with open(f_name,'r',encoding = 'utf-8') as f:
        for line in f:
            l.append(line.strip())
    return l
ans = 0
time1 = time.time()
file_name = input()
word_list = read_file(file_name)
for i in range(len(word_list)):
    str1 = word_list[i]
    str2 = str1[::-1]
    if str2 in word_list:
        ans += 1
time2 = time.time()
print(len(word_list))
print(ans)
print(time2- time1)