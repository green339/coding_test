# https://school.programmers.co.kr/learn/courses/30/lessons/120850
import re


def solution(my_string):
    return sorted(map(int, re.findall(r'\d', my_string)))
