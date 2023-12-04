from numpy import number
import pandas as pd
import numpy as np
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}
def replace_num(my_str):
    for key, value in help_dict.items():
         my_str = my_str.replace(key, value)
    return my_str

def check_string_forward(my_str):
    for i in range(len(my_str)):
        new_str=replace_num(my_str[0:i+1])
        if (new_str == my_str[0:i+1]):
            continue
        else:
            return new_str
        
def check_string_reverse(my_str):
    for i in range(len(my_str)):
        new_str=replace_num(my_str[-i-1:len(my_str)])
        # print(new_str, my_str[-i-1:len(my_str)])
        if (new_str == my_str[-i-1:len(my_str)]):
            continue
        else:
            return new_str
        
# filename="D:\\adventofcpde2022\\aoc2023\\data\\day1input.txt"
filename="D:\\adventofcpde2022\\aoc2023\\data\\day1ex1.txt"
# with open("D:\\adventofcpde2022\\aoc2023\\data\\day1ex.txt") as fp:
with open(filename) as fp:
    inlist = [line.rstrip('\n') for line in fp]
x=""
list=[]
for instr in inlist:
    # part 2 kicks in here - not so adorable code
    f=check_string_forward(instr)
    if (f is None):
        instr=instr
    else:
        r=check_string_reverse(instr)
        if (r is None):
            instr=f
        else:
            instr=f+r
    print(instr,f,r)
    #part 1 code - even this sucks - ideal way to do is get the first and last that should have been the solution 
    x=""
    for i in range(len(instr)):
        n=(instr[i:i+1])
        if (n.isnumeric()):
            x+=n
    list.append(x)

print(list)
sum=0
for num in list:
   s=int(num[0]+num[len(num)-1])
   sum+=s 
print(sum)