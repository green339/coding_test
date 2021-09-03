import sys

# 6_03 에서 모든 부분집합에서 합 구하기
# def dfs(d):
#     if d == N:
#         ans = 0
#         for i, j in zip(check, element):
#             ans += (i * j)
#         if not ans:
#             print("YES")
#             sys.exit(0)
#     else:
#         check[d] = 1
#         dfs(d + 1)
#         check[d] = -1
#         dfs(d + 1)

def dfs(d,s):
    if s>total//2:
        return
    if d==N:
        if total/2==s:
            print("YES")
            sys.exit(0)
    else:
        dfs(d+1,s+element[d])
        dfs(d+1,s)


N = int(sys.stdin.readline())
element = list(map(int, sys.stdin.readline().split()))
check = [-1] * N
total=sum(element)
if total % 2:
    print("NO")
else:
    dfs(0,0)
