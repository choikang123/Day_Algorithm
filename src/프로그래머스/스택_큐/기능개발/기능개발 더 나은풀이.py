def solution(progresses, speeds):
    stack = []
    answer = []

    for i in range(len(progresses)):
        # 1. 며칠 걸리는지 계산 (님의 완벽한 로직 그대로!)
        day = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            day += 1

        # 2. 스택(기준일)과 비교하기
        if not stack or day > stack[-1]:
            # 💡 [새로운 배포 그룹 탄생!]
            # 앞차보다 늦게 끝나면, 스택에 새 기준일을 넣고, answer에 "1개 배포" 방을 새로 만듦!
            stack.append(day)
            answer.append(1)
        else:
            # 💡 [앞차에 묻어가기!]
            # 앞차보다 일찍 끝나면? 새로 방을 만들 필요 없이, answer의 제일 '마지막 방'에 +1만 해줌!
            answer[-1] += 1

            # 3. 끝! (찜찜했던 0 지우기 for문이 아예 사라졌습니다!!)
    return answer