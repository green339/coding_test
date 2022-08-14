# https://school.programmers.co.kr/learn/courses/30/lessons/77486
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0] * n
    board = defaultdict(str)  # {구성원 : 추천인}
    answer_dic = defaultdict(int)
    for e, r in zip(enroll, referral):
        board[e] = r
    for s, a in zip(seller, amount):
        x = s
        money = a * 100
        while x != "-" and money > 0:
            give = int(money * 0.1)
            answer_dic[x] += money - give
            money = give
            x = board[x]
    for i in range(n):
        answer[i] = answer_dic[enroll[i]]
    return answer


def solution_v2(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    idx_dict = dict()
    for i in range(len(enroll)):
        idx_dict[enroll[i]] = i
    for s, a in zip(seller, amount):
        x = s
        money = a * 100
        while x != "-" and money > 0:
            x_idx = idx_dict[x]
            answer[x_idx] += money - money // 10
            money //= 10
            x = referral[x_idx]
    return answer
