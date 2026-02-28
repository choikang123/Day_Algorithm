import sys
from collections import defaultdict
input=sys.stdin.readline

n=int(input())
rec_count=int(input())
recommends=list(map(int,input().split()))

frames={}

for i,value in enumerate(recommends):
    # i=0, value=2
    if len(frames)>=n:
        if value in frames:
            frames[value][0]+=1
        else:
            target=min(frames,key=lambda x:(frames[x][0],frames[x][1]))
            del frames[target]
            frames[value]=[i+1]
    else:
        if value in frames:
            frames[value][0]+=1
        else:
            frames[value]=[1,i]

result=sorted(frames)
print(*result)