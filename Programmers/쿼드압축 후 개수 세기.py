# https://programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    def quad(sx, sy, l):
        flag = arr[sx][sy]
        for i in range(sx, sx + l):
            for j in range(sy, sy + l):
                if flag != arr[i][j]:
                    l //= 2
                    quad(sx, sy, l)
                    quad(sx + l, sy, l)
                    quad(sx, sy + l, l)
                    quad(sx + l, sy + l, l)
                    return
        answer[flag] += 1

    answer = [0, 0]
    quad(0, 0, len(arr))
    return answer
