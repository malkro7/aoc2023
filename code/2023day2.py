from numpy import number
import pandas as pd
import numpy as np
max_dict={
    "red":12,
    "green":13,
    "blue":14
}
def notViolation(instr):
    instr=instr.replace(";",",")
    games=[instr.split(",")]
    for game in games:
        for result in range(len(game)):
            outcome=[game[result].split()]
            if (int(outcome[0][0]) <= max_dict[outcome[0][1]]):
                continue
            else:
                return False
    return True
def minNumber(instr):
    instr=instr.replace(";",",")
    games=[instr.split(",")]
    min_dict={"red":0,"green":0,"blue":0}
    for game in games:
        for result in range(len(game)):
            outcome=[game[result].split()]
            if (int(outcome[0][0]) > min_dict[outcome[0][1]]):
                min_dict[outcome[0][1]] = int(outcome[0][0])
            else:
                continue
    return min_dict
filename="D:\\aoc2023\\data\\day2input.txt"
# filename="D:\\aoc2023\\data\\day2ex1.txt"
fp=open(filename,"r")
i=0
sum=0
for line in fp:
    i=i+1
    x=line.rstrip('\n').split(":")
    # part-1
    # if (notViolation(x[1])):
    #     sum=sum+i
    # part-2
    my_dict=minNumber(x[1])
    product=1
    for key, value in my_dict.items():
         product*= value
    sum+=product
print(sum)
