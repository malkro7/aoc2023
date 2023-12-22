from numpy import number
import pandas as pd
import numpy as np
import math
mapdict={}
alist=[]
count=0
rlseq=""
lcm=[]

filename="D:\\aoc2023\\data\\day8input.txt"

def buildmap(inlist):
    for r in inlist:
        r=r.replace(" = (",",").replace(")","").split(",")
        print(r)
        k=r[0]
        if (k[-1])=='A': alist.append(k)
        mapdict[k]=(r[1].strip(),r[2].strip())
            
def getnextkey(lr,word):
    
    try:
        l,r=mapdict[word]
        if (lr=='L'):
            nextkey = l
        else:
            nextkey = r
    except KeyError:
            nextkey = None
    return nextkey
def part2():
    lcm=[]
    for a in alist:
        k=a
        match=False
        cnt=0
        while (match==False):
  
            for char in lrseq:
                cnt+=1
                k1=getnextkey(char,k)
                if (k1=='ZZZ'):
                    match=True
                else:
                    k=k1
        lcm.append(cnt)
        print(a,cnt)
def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm
with open(filename) as fp:
    inlist = [line.rstrip('\n') for line in fp]
    lrseq=inlist[0]
    inlist.pop(0)
    inlist.pop(0)
    buildmap(inlist)
    print(alist)
    # k="QKA" 12169
    # k="VMA" 20093
    # k="AAA" 20659
    # k="RKA" 22357
    # k="LBA" 13301
    # k="JMA" 18961
    for a in alist:
        match=False
        cnt=0
        k=a
        while (match==False):
    
            for char in lrseq:
                cnt+=1
                k1=getnextkey(char,k)
                if (k1[-1]=='Z'):
                    match=True
                else:
                    k=k1
        lcm.append(cnt)
    print(LCMofArray(lcm))
    # part2()





            
    