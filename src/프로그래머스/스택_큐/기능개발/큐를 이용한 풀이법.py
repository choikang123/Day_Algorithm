from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque()

    # 1. 각 작업이 며칠 걸리는지 계산해서 큐(대기열)에 순서대로 줄 세우기!
    for p, s in zip(progresses, speeds):
        q.append(math.ceil((100 - p) / s))

    # 예제 1번이면 대기열(q)에 [7, 3, 9] 가 서 있는 상태입니다.

    # 2. 대기열(q)에 사람이 한 명이라도 남아있는 동안 계속 반복!
    while q:
        # 💡 핵심 1: 맨 앞차를 큐에서 뽑아냅니다! (기준일)
        front_day = q.popleft()
        count = 1 # 방금 뽑은 앞차 1대 배포!

        # 💡 핵심 2: 큐에 아직 차가 남아있고 && 그 다음 차(q[0])가 앞차보다 일찍 끝났다면?
        while q and q[0] <= front_day:
            q.popleft() # 너도 같이 나가!! (연속으로 큐에서 뽑아버림)
            count += 1  # 같이 나가는 개수 증가

        # 연속으로 쫙 다 뽑아냈으면, 묶음(count)을 정답에 찰칵!
        answer.append(count)

    return answer