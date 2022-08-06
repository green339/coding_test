# https://www.acmicpc.net/problem/11758
import sys

input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ccw = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

if ccw > 0:
    print(1)
elif ccw < 0:
    print(-1)
else:
    print(0)

'''
외적 - 신발끈 공식
오른손 법칙 - 검지>첫번째 벡터, 중지>두번째 벡터, 엄지>외적 방향
           엄지가 위로 올라 가면 양수: 반시계 방향
           엄지가 아래로 내려 가면 음수: 시계 방향
'''