# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    hash_list = {}
    for pn in phone_book:
        hash_list[pn] = 1
    for pn in phone_book:
        tmp = ""
        for element in pn:
            tmp += element
            if tmp == pn:
                continue
            if tmp in hash_list:
                return False
    return True


def solution_v2(phoneBook):
    phoneBook.sort()
    for p1, p2 in zip(phoneBook, phoneBook[1:]):  # 인접한 것 끼리 비교
        if p2.startswith(p1):
            return False
    return True

## 파이썬 스트링 startswith 메서드
