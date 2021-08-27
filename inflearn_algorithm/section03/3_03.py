import sys

cards = [i for i in range(1, 21)]
for _ in range(10):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    for i in range((b - a + 1) // 2):
        tmp = cards[a + i]
        cards[a + i] = cards[b - i]
        cards[b - i] = tmp
print(cards)
