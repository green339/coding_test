# https://programmers.co.kr/learn/courses/30/lessons/17686
import re


def solution(files):
    answer = []
    file_dict = dict()
    p1 = re.compile('\D+')
    p2 = re.compile('\d{1,5}')
    for idx, f in enumerate(files):
        head = p1.search(f)[0].lower()
        number = int(p2.search(f)[0])
        file_dict[idx] = (head, number)
    for i in sorted(file_dict.items(), key=lambda x: (x[1], x[0])):
        answer.append(files[i[0]])

    return answer
