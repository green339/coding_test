# https://school.programmers.co.kr/learn/courses/30/lessons/120849
def solution(my_string):
    vowel = ['a', 'e', 'o', 'i', 'u']
    for v in vowel:
        my_string = my_string.replace(v, '')
    return my_string
