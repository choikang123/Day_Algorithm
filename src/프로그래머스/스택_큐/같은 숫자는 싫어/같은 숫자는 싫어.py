def solution(arr):
    answer=[]

    for v in arr:
        if not answer:
            answer.append(v)
        else:
            if answer[-1]!=v:
                answer.append(v)
            else:
                continue

    return answer