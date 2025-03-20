import numpy as np
import pandas as pd
import time
import os
def save_file(filename,data):
    with open(filename,'w',encoding = 'utf-8') as f:
        for i in data:
            f.write(f'{str(i)}\n')
            
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
counter_pairs = []
self_pairs = []
for p in text:
    r_p = p[::-1]
    if(r_p == p):
        self_ans  = self_ans + 1
        self_pairs.append(p)
    else :
        if(r_p in text):
            ans = ans + 1
            if(r_p not in counter_pairs):
                counter_pairs.append(r_p)
                counter_pairs.append(p)
save_file('counter_pairs',counter_pairs)
save_file('self_pairs',self_pairs)
