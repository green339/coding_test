# https://programmers.co.kr/learn/courses/30/lessons/42579
from collections import defaultdict


def solution(genres, plays):
    answer = []
    genres_cnt = defaultdict(int)
    music = defaultdict(list)
    for i in range(len(genres)):
        genres_cnt[genres[i]] += plays[i]
        music[genres[i]].append((plays[i], i))
    for g in dict(sorted(genres_cnt.items(), key=lambda x: -x[1])).keys():
        answer.extend(list(zip(*sorted(music[g], key=lambda x: (-x[0], x[1]))))[1][:2])
    return answer
