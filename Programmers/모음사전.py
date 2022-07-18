# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 0
    diff = [781, 156, 31, 6, 1]
    alpha = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    for i in range(len(word)):
        answer += 1 + diff[i] * alpha[word[i]]
    return answer

# 노가다
def solution_v2(word):
    alpha = ["A", "E", "I", "O", "U", ""]
    arr = set()
    for x in alpha:
        for y in alpha:
            for j in alpha:
                for k in alpha:
                    for l in alpha:
                        arr.add(x + y + j + k + l)
    return sorted(arr).index(word)
