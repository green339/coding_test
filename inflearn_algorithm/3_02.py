import sys

case = sys.stdin.readline().strip()
num = []
for c in case:
    if c.isdigit():
        num.append(int(c))
x = 0
for i, n in enumerate(num[::-1]):
    x += (10 ** i) * n
count = 0
for i in range(1, x + 1):
    if x % i:
        continue
    count += 1
print(x, count)

# try/except ValueError로 int(c) 보다 isdigit() 이용
