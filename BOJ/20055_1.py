# https://www.acmicpc.net/problem/20055
# 2: 45
N, K = map(int, input().split())
A = list(map(int, input().split()))
l = 2 * N
cnt = 1
start = 0
end = N - 1
robot = [0] * l
while True:
    # 회전
    start = (start - 1) % l
    end = (end - 1) % l
    # 로봇들이 앞으로 한칸씩 이동
    if robot[end]:  # 내리는 위치 처리
        robot[end] = 0
    for i in range(end - 1, end - N, -1):
        if robot[i]:
            if not robot[i + 1] and A[i + 1] > 0:
                robot[i + 1] = 1
                robot[i] = 0
                A[i + 1] -= 1
    if robot[end]:  # 내리는 위치 처리
        robot[end] = 0
    # 올리는 위치에 로봇 올림
    if A[start] > 0:
        A[start] -= 1
        robot[start] = 1
    if A.count(0) >= K:
        break
    cnt += 1
print(cnt)
