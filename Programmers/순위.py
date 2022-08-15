# https://school.programmers.co.kr/learn/courses/30/lessons/49191
def solution(n, results):
    answer = 0
    board = [[0] * n for _ in range(n)]
    for a, b in results:
        board[a - 1][b - 1] = 1
    # A선수가 B선수보다 실력이 좋다면 A선수가 B선수를 항상 이김 (모든 경기 모순이 없다)
    # => i가 k를 이기고 k가 j를 이기면 i가 j를 이긴다
    # 플로이드 와샬(거쳐가는 경우)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][k] and board[k][j]:
                    board[i][j] = 1
    for b, bz in zip(board, zip(*board)):  # 이긴 횟수/ 진 횟수
        if sum(b) + sum(bz) == n - 1:
            answer += 1
    return answer
