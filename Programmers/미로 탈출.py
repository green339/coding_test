# https://programmers.co.kr/learn/courses/30/lessons/81304
from collections import defaultdict
from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)

def dfs(idx, cost, iin, oout):
    global answer
    print(idx,iin,oout)
    if idx == finish:
        print(answer)
        answer = min(answer, cost)

        return
    if idx in trap:
        for ob, oc in oout[idx]:
            print(idx,ob,oc)
            oout[ob].append((idx,oc))
            iin[ob].remove((idx,oc))

        tmp = deepcopy(iin[idx])
        iin[idx] = deepcopy(oout[idx])
        oout[idx] = deepcopy(tmp)
    for b, c in iin[idx]:
        dfs(b, cost + c, iin, oout)


def solution(n, start, end, roads, traps):
    global finish, answer,trap
    trap=set(traps)
    finish = end
    answer = 1e9
    board_in = defaultdict(list)
    board_out = defaultdict(list)
    for a, b, c in roads:
        board_in[a].append((b, c))
        board_out[b].append((a,c))
    dfs(start, 0, board_in, board_out)
    print("!!!!",answer)
    return answer


solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
