from collections import deque


def solution(rc, operations):
    def func(flag, k):
        if flag == "ShiftRow":
            k %= row
            rc.rotate(k)
        else:
            total = 2 * row + 2 * col - 4
            print(total)
            k %= total
            print(rc[-1])
            if k==total/2:
                tmp=rc[-1]
                rc[-1]=deque(reversed(rc[0]))
                rc[0]=deque(reversed(tmp))
                print(rc)
                for i in range(1,row-1):
                    tmp=rc[0][i]
                    rc[i][0]=rc[row-i-1][-1]
                    rc[row-i-1][-1]=tmp
            else:
                i=0
                j=0
                tmp=0
                change=0
                # while change<total:

    answer = [[]]
    rc = deque(deque(r) for r in rc)
    row = len(rc)
    col = len(rc[0])
    prior = ''
    cnt = 0
    for op in operations:
        if op != prior and cnt:
            func(op, cnt)
            cnt = 1
            prior = op
        else:
            cnt += 1
            prior = op
    print(prior, cnt)
    func(prior, cnt)
    print(rc)
    return answer

solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],["Rotate", "Rotate", "Rotate", "Rotate"])