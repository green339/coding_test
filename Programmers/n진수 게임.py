# https://programmers.co.kr/learn/courses/30/lessons/17687

def notation(x, dnum):
    ans = ''
    ch = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C",
          13: "D", 14: "E", 15: "F"}
    while dnum > 0:
        ans += ch[dnum % x]
        dnum //= x
    return ans[::-1] if ans else "0"


def solution(n, t, m, p):
    answer = ''
    string = ''
    number = 0
    while len(string) <= t * m:
        string += notation(n, number)
        number += 1
    for s in range(p - 1, t * m, m):
        answer += string[s]
    return answer
