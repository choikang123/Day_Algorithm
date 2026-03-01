from collections import defaultdict
from collections import Counter
def solution(phone_book):
    # 딕셔너리를 만들어주는 3가지 방법
    dic_phone_book1=defaultdict(int)
    for phone in phone_book:
        defaultdict[phone]

    dict={}
    for phone in phone_book:
        if phone in dict:
            dict[phone]+=1
        else:
            dict[phone]=1

    dic_phone_book3=Counter(phone_book)

    # 각 전화번호 한번씩 딕셔너리에 있는지 확인 o(n) 시간 복잡도
    for phone in (phone_book):
        # phone 1부터 길이까지 하나씩 늘려가면서 슬라이싱해주기
        for i in range(len(phone)):
            # 0  1    2
            # 9  97  976
            if phone[:i] in dict:
                return False #궁금한거 return하면 for문 밖의 for문도 반환되는건지

    return True