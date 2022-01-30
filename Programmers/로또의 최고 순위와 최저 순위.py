# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    count_zero = lottos.count(0)
    same = len(set(lottos) & set(win_nums))
    answer = [rank[same + count_zero], rank[same]]
    return answer
