def solution(clothes):
    dict={}

    answer=1
    for value in clothes:
        if value[1] in dict:
            dict[value[1]]+=1
        else:
            dict[value[1]]=1

    answer=1
    for key in dict:
        answer*=dict[key]+1

    answer-=1
    return answer