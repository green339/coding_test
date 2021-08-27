import sys

N = int(sys.stdin.readline())
ans = []
for _ in range(N):
    case = sys.stdin.readline().strip().lower()
    l = len(case)
    flag = 1
    for i in range(l // 2):
        if case[i] != case[l - i]:
            flag = 0
            break
    if flag:
        ans.append("YES")
    else:
        ans.append("NO")
    # if case==case[::-1]:
    #     ans.append("YES")
    # else:
    #     ans.append("NO")
for k, a in enumerate(ans):
    print(f'#{k + 1} {a}')
