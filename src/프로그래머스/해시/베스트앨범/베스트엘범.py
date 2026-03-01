from collections import defaultdict
def solution(genres, plays):
    # 장르별로 합해서 정렬
    # 최대 2개까지 plays가 많은 순서로 뽑아주기

    # 순서 정렬을 위한 딕셔너리
    genre_dict=defaultdict(list)
    # 합을 담을 딕셔너리
    sum_dict=defaultdict(int)

    for i in range(len(plays)):
        genre_dict[genres[i]].append([plays[i],i])
        sum_dict[genres[i]]+=plays[i]
    # classic: [500,0],[150,2],[800,3]
    # pop: [600,1],[2500,4]

    sorted_genres=sorted(sum_dict.keys(), key=lambda x:-sum_dict[x])
    # 정렬 이후: [pop:3100,classic:1450]

    for genre in genre_dict:
        genre_dict[genre].sort(key=lambda x:-x[0])

    answer = []
    for genre in sorted_genres:
        for value,index in genre_dict[genre][:2]:
            answer.append(index)
    return answer