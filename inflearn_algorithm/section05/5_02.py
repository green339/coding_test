import sys

laser = sys.stdin.readline().strip()
stack = 0
ans = 0
for l in laser:
    if l == "(":
        stack += 1
        last = "("
    else:
        stack -= 1
        if last == ")":
            ans += 1
        else:
            ans += stack
        last = ")"
print(ans)
