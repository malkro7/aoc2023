from numpy import number
import pandas as pd
import numpy as np
master_dict={}
def getwincount(instr):
    winning_dict={}
    count=0
    instr=[instr.split("|")]
    draws=instr[0][0].split()
    wins=instr[0][1].split()
    for win in wins:
        winning_dict[win]=1
    
    for draw in draws:
        try:
            count+=winning_dict[draw]
        except KeyError: 
            count+=0
    return count
filename="D:\\aoc2023\\data\\day4input.txt"
# filename="D:\\aoc2023\\data\\day4ex1.txt"
fp=open(filename,"r")
i=0
sum=0
for line in fp:
    i=i+1
    x=line.rstrip('\n').split(":")
    n=getwincount(x[1])
    if n>0:
        sum=sum+2**(n-1)
    master_dict[i]=n
new_master_dict={}
tmplist=[]
newsum=0
def recurfunc(skey):
    for z in range(master_dict[skey]):
        tmplist.append(skey+z+1)
        recurfunc(skey+z+1)
print(master_dict)
for key, values in master_dict.items():
        tmplist=[key]
        for r in range(values):
            tmplist.append(key+r+1)
            recurfunc(key+r+1)
        newsum+=len(tmplist)
# for key, values in new_master_dict.items():
#     newsum+=values
print(newsum)

