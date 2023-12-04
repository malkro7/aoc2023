from numpy import number
import pandas as pd
import numpy as np

filename="D:\\aoc2023\\data\\day5input.txt"
# filename="D:\\aoc2023\\data\\day5ex1.txt"
fp=open(filename,"r")
i=0
sum=0
for line in fp:
    i=i+1
    x=line.rstrip('\n').split(":")


