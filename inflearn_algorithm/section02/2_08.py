import sys


def reverse(x):
    return int(x[::-1])


def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if not x % i:
            return False
    return True


N = int(sys.stdin.readline())
ans = []
for k in map(str, sys.stdin.readline().split()):
    tmp = reverse(k)
    if isPrime(tmp):
        ans.append(tmp)
print(*ans)
