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
