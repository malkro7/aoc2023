from numpy import number
import pandas as pd
import numpy as np
max_dict={}
filename="D:\\aoc2023\\data\\day3input.txt"
# filename="D:\\aoc2023\\data\\day3ex1.txt"
fp=open(filename,"r")
lines=fp.readlines()
sum=0
map_dict={}
sumlist=[]
prdlist=[]
def getleft(key):
    l=""
    x=key[0]
    y=key[1]
    while (y>1):
        y=y-1
        val=map_dict[(x,y)]
        if (val.isnumeric()):
            l+=val
        else:
            return(l[::-1])
    return(l[::-1])
def getright(key):
    r=""
    x=key[0]
    y=key[1]
    while (y<140):
        y=y+1
        val=map_dict[(x,y)]
        if (val.isnumeric()):
            r+=val
        else:
            return(r)
    return(r)
def getabove(key):
    a=""
    x=key[0]
    y=key[1]
    val=map_dict[x-1,y]
    if (val.isnumeric()):
        a=getleft((x-1,y))+val+getright((x-1,y))
    else:
        val=map_dict[(x-1,y-1)]
        if (val.isnumeric()):
            a=(getleft((x-1,y)))
        val=map_dict[(x-1,y+1)]
        if (val.isnumeric()):
            a=a+","+(getright((x-1,y)))
    return(a)
def getbelow(key):
    b=""
    x=key[0]
    y=key[1]
    val=map_dict[x+1,y]
    if (val.isnumeric()):
        b=(getleft((x+1,y))+val+getright((x+1,y)))
    else:
        val=map_dict[(x+1,y-1)]
        if (val.isnumeric()):
            b=(getleft((x+1,y)))
        val=map_dict[(x+1,y+1)]
        if (val.isnumeric()):
            b=b+","+(getright((x+1,y))) 
    return(b)
def buildmap(lines):
    x=0
    for line in lines:
        x=x+1
        y=0
        for char in line.rstrip("\n"):
            y=y+1
            if((char=='.') | (char.isnumeric())):
                map_dict[(x,y)]=char
            elif((char=="*")):
                map_dict[(x,y)]="*"
            else:
                map_dict[(x,y)]="$"
maxrows=len(lines)
buildmap(lines)

for key, value in map_dict.items():
    tmplist=[]
    if(value=="*"):
        l=getleft(key)
        if (l.isnumeric()): 
            sumlist.append(int(l))
            tmplist.append(int(l))

        r=getright(key)
        if (r.isnumeric()): 
            sumlist.append(int(r))
            tmplist.append(int(r))

        if (key[0] > 1):
            a=getabove(key)
        A=a.split(",")
        if (A[0].isnumeric()):
            sumlist.append(int(A[0]))
            tmplist.append(int(A[0]))
        if len(A) > 1:
            if (A[1].isnumeric()):
                sumlist.append(int(A[1]))
                tmplist.append(int(A[1]))

        if (key[0] < maxrows):
            b=getbelow(key)
        B=b.split(",")
        if (B[0].isnumeric()):
            sumlist.append(int(B[0]))
            tmplist.append(int(B[0]))
        if len(B) > 1:
            if (B[1].isnumeric()):
                sumlist.append(int(B[1]))
                tmplist.append(int(B[1]))
        if(len(tmplist)==2):
            prdlist.append(tmplist[0]*tmplist[1])

print(prdlist)
for n in sumlist:
    sum+=n
print(sum)
for p in prdlist:
    sum+=p
print(sum)

    




