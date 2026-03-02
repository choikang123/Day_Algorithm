def solution(progresses, speeds):
    stack = []
    answer= []
    count = [0]*101
    # progresses=[93, 30, 55]
    for i in range(len(progresses)):
        # 작업 완료까지 걸리는 기간계산
        day=0
        while progresses[i]<100:
            progresses[i]+=speeds[i]
            day+=1
        # 앞에 있는 기능이 완성되지 않으면 배포가 불가능
        # 스택에 값이 있고 즉 2번째부터 다음 작업이 이전 작업보다 더 빨리 끝난다면
        print(day)
        if not stack:
            stack.append(day)
            count[day]+=1
        else:
            if day<=stack[-1]:
                count[stack[-1]]+=1
            elif day>stack[-1]:
                old_day=stack.pop()
                stack.append(day)
                count[day]+=1
    # 스택에 남은 값이 있으면 빼주기
    for value in count:
        if value!=0:
            answer.append(value)

    return answer