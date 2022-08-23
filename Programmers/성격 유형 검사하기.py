# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    answer = ['R', 'C', 'J', 'A']
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
                   'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for s, c in zip(survey, choices):
        if c > 4:
            personality[s[1]] += c - 4
        else:
            personality[s[0]] += 4 - c
    if personality['R'] < personality['T']:
        answer[0] = 'T'
    if personality['C'] < personality['F']:
        answer[1] = 'F'
    if personality['J'] < personality['M']:
        answer[2] = 'M'
    if personality['A'] < personality['N']:
        answer[3] = 'N'
    return ''.join(answer)
