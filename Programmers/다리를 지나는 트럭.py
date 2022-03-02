# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    in_time = deque()  # 들어간 시간
    last = 1  # 마지막으로 나간 시간
    bw = 0  # 다리 무게
    for truck in truck_weights:
        cnt = 0
        while bw + truck > weight or len(bridge) + 1 > bridge_length: # 이번 타임에 트럭이 들어올 수 있도록 정리
            bw -= bridge.popleft()
            last = in_time.popleft() + bridge_length
            cnt += 1
        bridge.append(truck)
        bw += truck
        if not cnt:  # 처음이거나 연속해서 들어오는 경우
            if in_time:  # 연속해서
                in_time.append(in_time[-1] + 1)
            else:  # 처음
                in_time.append(last)
        else:
            in_time.append(last)
        '''
        in_time[-1]이 현재 시간
        현재 시간 기준으로 다리에서 나갔어야 하는 트럭들을 빼고 last를 갱신 해줌
        '''
        while in_time[-1] - in_time[0] >= bridge_length:
            bw -= bridge.popleft()
            last = in_time.popleft() + bridge_length
    return in_time[-1] + bridge_length
