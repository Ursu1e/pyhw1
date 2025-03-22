import numpy 
import os
def read_file(file_name):
    l = list()
    with open(file_name,'r') as f:
        for line in f:
            l.append(line.strip())
    return l
def list_to_dict(l):
    d = dict()
    for i in l:
        if i in d:
            d[i] += 1
        else :
            d[i] = 1
    return d
print("enter the filename you want to read:")
str1 = input()
word_list = read_file(str1)
word_dict = list_to_dict(word_list)
print(word_dict)
print("Here is a test the whole program:")
print('and you need to input a number n for the word you want to check\nn:')
n = int(input())
dict1 = dict()
test_list = list()
for i in range(n):
    word_1 = input()
    test_list.append(word_1)
test_dict = list_to_dict(test_list)
print(test_dict)
