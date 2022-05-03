# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = s
    numword = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
               "eight": "8", "nine": "9"}
    for k, v in numword.items():
        answer = answer.replace(k, v)
    return int(answer)


def solution_v2(s):
    number = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
              "eight": "8", "nine": "9", "zero": "0"}
    for k, v in number.items():
        s = s.replace(k, v)
    return int(s)
