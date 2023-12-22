from numpy import number
import pandas as pd
import numpy as np

def differences(numbers):
    while any(numbers):
        differences = [b - a for a, b in zip(numbers[:-1], numbers[1:])]
        yield differences
        numbers = differences

def getnumbers(numbers):
        tmp=0
        prev=0
        next=0
        for item in reversed(my_arrays):
            l=len(item)
            tmp=item[l-1]
            if(tmp==0):
                continue
            else:
                curr=tmp+prev
                prev=curr
            print(item,curr,prev)

filename="D:\\aoc2023\\data\\day9ex1.txt"
with open(filename) as fp:
    inlist = [list(map(int,line.rstrip('\n').split())) for line in fp]
global numbers
numbers=[1,2,3,4,5]
my_arrays=[]
new_numbers=[1]
while sum(new_numbers)!=0:
    for i in range(len(numbers)-1):
        new_numbers=[numbers]
        new_numbers.append(numbers[i+1]-numbers[i])
     
# # for array in inlist:
# #      for differences in differences(list(numbers)):
# #         print(differences)
# for i in range(2):
#     for differences in differences(numbers):
#         print(differences)