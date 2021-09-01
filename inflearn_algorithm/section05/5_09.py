import sys

words = sys.stdin.readline().strip() + sys.stdin.readline().strip()
temp = 0
for w in words:
    temp ^= ord(w)
if temp:
    print("NO")
else:
    print("YES")
