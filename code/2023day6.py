from numpy import number
import pandas as pd
import numpy as np
time=[44806572]
dist=[208158110501102]
cnt=0
prd=1
for o in range(len(time)):
    t=int(time[o])
    print(t,dist[o])
    cnt=0
    for i in range(1,t,1):
        if((t-i)*i)>int(dist[o]):
            cnt+=1
    prd*=cnt
print(prd)

