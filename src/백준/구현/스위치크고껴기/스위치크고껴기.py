import sys
input=sys.stdin.readline

#8
t=int(input())
#0 1 0 1 0 0 0 1
switches=list(map(int,input().split()))
#2
n=int(input())

for _ in range(n):
    # s=1 c=3
    s,num=map(int,input().split())

    if s==1:
        # c=4 일때, 4와 8의 인덱스 스위치가 바뀌어야 한다
        # 0 1 2 3 4 5 6 7
        for i in range(num-1,len(switches),num):
            if switches[i]==0:
                switches[i]=1
            elif switches[i]==1:
                switches[i]=0
    else:
        #c=3 이면 실제 인덱스는 2이고 양옆은 1과 3
        index=num-1
        left=index-1
        right=index+1

        while left>=0 and right<len(switches) and switches[left]==switches[right]:
            switches[left]=1-switches[left]
            switches[right]=1-switches[right]

            left-=1
            right+=1

        switches[index]=1-switches[index]

for i in range(0,len(switches),20):
    print(*switches[i:i+20])



