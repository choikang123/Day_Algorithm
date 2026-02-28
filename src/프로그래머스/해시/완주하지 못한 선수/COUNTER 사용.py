import collections

def solution(participant, completion):
    # 1. 참가자 명단을 {이름: 개수} 딕셔너리로 변신!
    part_counter = collections.Counter(participant)

    # 2. 완료자 명단을 {이름: 개수} 딕셔너리로 변신!
    comp_counter = collections.Counter(completion)

    # 3. 참가자 딕셔너리에서 완료자 딕셔너리를 빼버립니다!
    answer = part_counter - comp_counter

    # answer 상태: Counter({'mislav': 1})

    # 4. 남은 한 명의 이름을 뽑아서 리턴! (딕셔너리의 키값들 중 첫 번째)
    return list(answer.keys())[0]