def solution(participant, completion):
    participant_dic={}

    for person in participant:
        if person in participant_dic:
            participant_dic[person]+=1
        else:
            participant_dic[person]=1

    for c in completion:
        if c in participant_dic:
            participant_dic[c]-=1

    for k,v in participant_dic.items():
        if v==1:
            return k


# def solution(participant, completion):
#     attendance_book = {} # 텅 빈 출석부(딕셔너리) 준비
#
#     # 1. 참가자들을 전부 출석부에 적습니다. (이름: 사람 수)
#     for p in participant:
#         if p in attendance_book:
#             attendance_book[p] += 1 # 동명이인이면 숫자를 +1
#         else:
#             attendance_book[p] = 1  # 처음 적는 이름이면 1명
#
#     # 현재 attendance_book 상태 (예제 3번):
#     # {"mislav": 2, "stanko": 1, "ana": 1}
#
#     # 2. 완료자 명단을 보면서 출석부에서 1명씩 빼줍니다. (줄 긋기)
#     for c in completion:
#         attendance_book[c] -= 1
#
#     # 지운 후 attendance_book 상태:
#     # {"mislav": 1, "stanko": 0, "ana": 0}
#
#     # 3. 출석부를 쫙 훑어보면서, 값이 0이 아닌(즉, 1로 남아있는) 단 한 명을 찾습니다!
#     for key, value in attendance_book.items():
#         if value == 1:
#             return key # 범인 검거 완료!





