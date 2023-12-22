from numpy import number
import pandas as pd
import numpy as np
import concurrent.futures

# filename="D:\\aoc2023\\data\\day5exbp.txt"
filename="D:\\aoc2023\\data\\day7input.txt"

order_dict={
    'A':14,
    'K':13,
    'Q':12,
    'J':1,
    'T':10,
    '9':9,
    '8':8,
    '7':7,
    '6':6,
    '5':5,
    '4':4,
    '3':3,
    '2':2
     }
fp=open(filename,"r")
winning_dict={}
listofhands=[]

def evalhand(string, score):
    # Counting every characters of the string
    jtrue=False
    count={} 
    hattr=[string, int(score)]
    
    for s in string:
        hattr.append(order_dict[s]) 
        if(s=='J'): jtrue=True
        try:
            count[s]+=1
        except KeyError:
            count[s]=1
   
    tmp=0
    if (jtrue):
        jcount=count['J']
        del count['J']
        if len(count)>0:
            max_value=max(count.values())+jcount
        else:
            count['A']=5
    else:
        max_value=max(count.values())

    print(count)
    l=len(count)
    
    if(l==1):
        hattr.append(6)
    elif (l==2):
        if(max_value==4):
            hattr.append(5)
        else:
            hattr.append(4)
    elif(l==3):
        if(max_value==3):
            hattr.append(3)
        else:
            hattr.append(2)
    elif (l==4):
        hattr.append(1)
    else:
        hattr.append(0)

    listofhands.append((hattr))
            
for line in fp.readlines():
    evalhand((line.strip('\n').split()[0]),(line.split()[1]))

# print(listofhands)
cards=sorted(listofhands,key=lambda x:(x[7],x[2],x[3],x[4],x[5],x[6]),reverse=False)
print(cards)
i=1
sum=0
for card in cards:
    print(i,card[1],card[7])
    sum+=i*card[1]
    i=i+1
print(sum)

# df=pd.DataFrame(listofhands,columns=['hand','score','p1','p2','p3','p4','p5','kind'])
# dfs=df.sort_values (['kind','p1','p2','p3','p4','p5'])
# i=1
# for row in dfs.iterrows():
#     print(i,dfs['score'])
#     i+=1
