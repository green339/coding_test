def solution(cap, n, deliveries, pickups):
    answer = 0
    deli_move = n
    pick_move = n
    while deli_move > 0 or pick_move > 0:
        print(deli_move, pick_move)
        answer += max(deli_move, pick_move) * 2
        deli_cnt = 0
        for i in range(deli_move - 1, -1, -1):
            if deli_cnt + deliveries[i] <= cap:
                deli_cnt += deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= (cap - deli_cnt)
                deli_move = i + 1
                break
        else:
            deli_move=0
        pick_cnt = 0
        for i in range(pick_move - 1, -1, -1):
            if pick_cnt + pickups[i] <= cap:
                pick_cnt += pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= (cap - pick_cnt)
                pick_move = i + 1
                break
        else:
            pick_move=0

    return answer

solution(4,5,[1,0,3,1,2],[0,3,0,4,0])