# https://school.programmers.co.kr/learn/courses/30/lessons/92345
def solution(board, aloc, bloc):  # 반환: 결과(승:1,패:0) / 현재(시작X)~종료 시점까지의 적절한 이동수
    def dfs(flag):
        x, y = player[flag]
        if not board[x][y]:  # 발판이 0인 경우 -> 패
            return 0, 0
        result = [[], []]  # 주변을 탐색 -> 반환값 저장 [0:승 1:패]
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if -1 < nx < r and -1 < ny < c:
                if board[nx][ny] == 1:
                    board[x][y] = 0
                    player[flag] = [nx, ny]
                    game, move = dfs(abs(flag - 1))
                    result[game].append(move + 1)
                    board[x][y] = 1
                    player[flag] = [x, y]
        if not result[0] and not result[1]:  # 주변으로 이동 불가 -> 패
            return 0, 0
        elif result[0]:  # 한 번이라도 이긴 경우
            return 1, min(result[0])
        elif result[1]:  # 계속 진 경우
            return 0, max(result[1])

    r = len(board)
    c = len(board[0])
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    player = [aloc, bloc]
    answer = dfs(0)[1]
    return answer
'''
백트래킹에서는 마지막에 answer와 비교를 하는 방법을 주로 사용 (return 값 신경 안쓰고)
이 경우에는 return 값에 대해 고려하는 것이 중요
-> 종료 지점은 항상 패 할 수밖에 없음 + 더 이상의 이동이 불가(1. 발판이 없거나 2.주변으로 이동 불가)
"최적의 플레이를 한다" -> 해당 자리로 이동을 한 결과(반환값)을 가지고 최선의 선택을 한다.
    - 반환된 결과가 다 졌으면 -> (움직이는 횟수 최대화) 진 결과값 중에서 최대 횟수를 반환
    - 반환된 결과 중 하나라도 이겼으면 -> (움직이는 횟수 최소화) 이긴 결과값 중에서 최소 횟수를 반환
위의 코드에서는 반환값과 결과 배열 반대가 됨(상대방 결과 그대로 저장)
    상대방의 결과: 패 -> 본인 결과: 승
    result[game]->result[~game]으로 저장하면 항상 승:1 패:0으로 생각할 수 있음
'''