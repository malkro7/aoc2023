def getsol(cfg, nums):

    if cfg == "":
      return 1 if nums == () else 0
    if nums==():
      return 0 if "#" in cfg else 1
    num=0
    if cfg[0] in "#?":
        num+=getsol(cfg[1:],nums)
    if (int(nums[0])<=len(cfg)) and "." not in cfg[:int(nums[0])] and (nums[0] == len(cfg) or cfg[int(nums[0])] != "#"):
        num+=getsol(cfg[int(nums[0])+1:],nums[1:])
    else:
        num+=0
    return num

filename="D:\\aoc2023\\data\\day12ex1.txt"
fp=open(filename,"r")
lines=fp.readlines()
total=0
for line in lines:
    sym, pos = line.strip("\n").split()
    print(type(sym), type(pos))
    post=tuple(map(int,pos.split(",")))
    total+=getsol(cfg=sym,nums=pos)
