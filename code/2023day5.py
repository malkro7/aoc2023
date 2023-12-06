from numpy import number
import pandas as pd
import numpy as np
import concurrent.futures

seed2soil=[]
soil2fert=[]
fert2water=[]
water2light=[]
light2temp=[]
temp2hum=[]
hum2loc=[]

# filenames=["D:\\aoc2023\\data\\day5exstos.txt","D:\\aoc2023\\data\\day5exstof.txt","D:\\aoc2023\\data\\day5exftow.txt","D:\\aoc2023\\data\\day5exwtol.txt","D:\\aoc2023\\data\\day5exltot.txt","D:\\aoc2023\\data\\day5exttoh.txt","D:\\aoc2023\\data\\day5exhtol.txt"]
filenames=["D:\\aoc2023\\data\\day5ipstos.txt","D:\\aoc2023\\data\\day5ipstof.txt","D:\\aoc2023\\data\\day5ipftow.txt","D:\\aoc2023\\data\\day5ipwtol.txt","D:\\aoc2023\\data\\day5ipltot.txt","D:\\aoc2023\\data\\day5ipttoh.txt","D:\\aoc2023\\data\\day5iphtol.txt"]
# filename="D:\\aoc2023\\data\\day5ex1.txt"
# seeds=[79,14,55,13]
seeds=[4088478806, 114805397, 289354458, 164506173, 1415635989, 166087295, 1652880954, 340945548, 3561206012, 483360452, 35205517, 252097746, 1117825174, 279314434, 3227452369, 145640027, 2160384960, 149488635, 2637152665,236791935]
def buildmap(filename,listname):
    fp=open(filename,"r")
    for line in fp:
        x=line.rstrip('\n').split(" ")
        sdi=(int(x[1]),int(x[0]),int(x[2]))
        listname.append(sdi)
    fp.close()

def findloc(skey,listname):
    for tup in listname:
        src,dest,inc=tup
        if (skey>=src)&(skey<=src+inc):
            return(dest+(skey-src))
    return skey
tmplist=[]
def seedsoil(skey1,skey2,listname):
    print(skey1,skey2)
    # 79,80,81,82,83,84,85,86,87,88,89,90,91,92  98,99 51,52
    # 55,56,57,58,59,60,61,62,63,64,65,66,67     50-97, 52-99  79-14, 81 to 94

    for tup in listname:
        src,dest,inc=tup
        print(tup)
        destxy=()
        if (skey1>=src):
            if (inc>(skey1-src)):
                destxy=(dest+skey1-src,dest+skey1-src+skey2-1)
                tmplist.append(destxy)
        
buildmap(filenames[0], seed2soil)
buildmap(filenames[1], soil2fert)
buildmap(filenames[2], fert2water)
buildmap(filenames[3], water2light)
buildmap(filenames[4], light2temp)
buildmap(filenames[5], temp2hum)
buildmap(filenames[6], hum2loc)
k=0
while k<len(seeds):
    seedsoil(seeds[k],seeds[k+1],seed2soil)
    k=k+2
print(tmplist)
seedtoloc=[]
for tup in tmplist:
    if len(tup)>0:
        lb,ub=tup
        while (lb<=ub):
            with concurrent.futures.ProcessPoolExecutor() as executor:
                loc=findloc(findloc(findloc(findloc(findloc(findloc(lb,soil2fert),fert2water),water2light),light2temp),temp2hum),hum2loc)
                lb+=1
                seedtoloc.append(loc)
print(min(seedtoloc))

# for i in seeds:
#     loc=findloc(findloc(findloc(findloc(findloc(findloc(findloc(i,seed2soil),soil2fert),fert2water),water2light),light2temp),temp2hum),hum2loc)
#     seedtoloc.append(loc)
# print(min(seedtoloc))
new=[]
def locranges(seedstart,seedend,ranges):
    for start, end, inc in ranges:
            linestart = max(seedstart, end)
            lineend = min(seedend, end + inc)
            if linestart < lineend:
                new.append((linestart - end + start, lineend - end + a))
                if linestart > s:
                    seeds.append((seedstart, linestart))
                if e > lineend:
                    seeds.append((lineend, seedend))
                break
            else:
                new.append((seedstart, seedend))
    seeds = new

print(min(seeds)[0])
seeds=[4088478806, 114805397, 289354458, 164506173, 1415635989, 166087295, 1652880954, 340945548, 3561206012, 483360452, 35205517, 252097746, 1117825174, 279314434, 3227452369, 145640027, 2160384960, 149488635, 2637152665,236791935]
for k in len(seeds):
    