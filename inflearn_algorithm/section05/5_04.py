import sys

exp = sys.stdin.readline().strip()
num = []
for e in exp:
    if e.isdigit():
        num.append(e)
    else:
        b = num.pop()
        a = num.pop()
        num.append(str(eval(a + e + b)))
print(int(num.pop()))
