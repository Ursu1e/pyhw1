import numpy as np
import pandas as pd
import time
import os     
start_time = time.time()
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,'words.txt')
if not os.path.exists(file_path):
    print("the file 'words.txt' is not under your dir (you may enter the wrong filename)")
    exit()
# read_file_time = time.time()
text = list()
ans = self_ans = 0
with open(file_path,'r') as f:
    for line in f:
        text.append(line.strip())
read_file_time = time.time()
print(f'读取文件所花费的时间是{read_file_time - start_time}')
text = set(text)
for p in text:
    r_p = p[::-1]
    if(r_p == p):
        self_ans  = self_ans + 1
    else :
        if(r_p in text):
            ans = ans + 1
ed_time = time.time()
print(f'完成任务所需要的时间是:{ed_time - read_file_time}')
print(f'总共的单词数:{len(text)}\n互为回文串对:{ans/2}\n自身为回文串数:{self_ans}')
