# https://school.programmers.co.kr/learn/courses/30/lessons/120851
import re


def solution(my_string):
    return sum(map(int, re.findall(r'\d', my_string)))
