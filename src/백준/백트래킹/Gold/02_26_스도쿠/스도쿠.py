import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

board=[list(map(int,input().split())) for _ in range(9)]
# 숫자가 들어가지 않은 좌표 r,c가 들어가 있다
blank=[]

def check(r,c,i):
    # 가로줄 세로줄에서 숫자 i 가 1-9중에 겹치는게 없는지 확인
    # 가로줄이면 r은 고정
    for k in range(9):
        # 임의로 정한 값 i와 해당 행의 가로줄에 있는 값인지
        if board[r][k]==i or board[k][c]==i:
            # 있다면 함수 반환
            return False

    # 3*3 네모 칸
    # 네모 칸의 왼쪽 맨위 즉 시작점을 먼저 찾아준다
    # 시작 행과 열
    start_row=(r//3)*3
    start_column=(c//3)*3

    # (0,0) (0,1) (0,2)
    # (1,0)
    # (2,0)
    # 0,3
    for row in range(start_row,start_row+3):
        for col in range(start_column,start_column+3):
            if board[row][col]==i:
                return False

    # 3가지 조건이 아니라면 값이 들어갈 수 있음
    return True

def dfs(depth):
    # 기저 조건 깊이와 blank의 갯수가 같아질때까지
    if depth==len(blank):
        for row in board:
            print(*row)
        sys.exit(0)

    # blank 리스트에서 하나씩 해당 깊이의 좌표 꺼내기
    r,c=blank[depth]

    # 1부터 9까지의 숫자중에 해당 좌표가 조건에 만족하는 경우 더 깊이 들어가기
    for i in range(1,10):
        if check(r,c,i):
            board[r][c]=i
            dfs(depth+1)
            board[r][c]=0

for r in range(9):
    for c in range(9):
        if board[r][c]==0:
            blank.append((r,c))

dfs(0)


