from collections import defaultdict
hmaster=[]
vmaster=[]
mat=[]
sum=0
def build_dict(source,vh):
    target=defaultdict(tuple)
    for key in source:
        target[source[key]] +=(key,)
    # sorted_target = sorted(target.items(), key=lambda x:x[1])
    if vh=="h":
        hmaster.append(target)
    else:
        vmaster.append(target)
def computesum(row):
    tmp={v:k for k,v in row.items() if len(v)== 2}
    l=[]
    for key, value in tmp.items():
        l.append(int(key[1])-int(key[0]))
        l.sort(reverse=False)
        cnt=0
        for i in range(len(l)-1):
            if (l[i+1]-l[i]==2):
                cnt+=1
            else:
                cnt+=0
    return(cnt)


with open("data\\day13input.txt", "r") as file:
    data = file.read().strip()

    blocks = data.split("\n\n")
    for block in blocks:
        hmat=block.split("\n")
        vmat=[''.join(s) for s in zip(*hmat)]
        i=0
        source={}
        for h in hmat:
            i+=1
            source[i]=h
        build_dict(source,"h")
        i=0
        for v in vmat:
            i+=1
            source[i]=v
        build_dict(source,"v")
        for i in range(len(vmaster)):
            sum+=computesum(vmaster[0])*100
            
            sum+=computesum(vmaster[0])
    print(sum)




           
        

        

        