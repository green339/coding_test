import sys

exp = sys.stdin.readline().strip()
ans = []
op = []
for e in exp:
    if e == "(":
        op.append(e)
    elif e == ")":
        while True:
            print(op)
            o = op.pop()
            if o == "(":
                break
            ans.append(o)
    elif e == "*" or e == "/":
        while op and (op[-1] == "*" or op[-1] == "/"):
            ans.append(op.pop())
        op.append(e)
    elif e == "+" or e == "-":
        while op and op[-1]!="(":
            ans.append(op.pop())
        op.append(e)
    else:
        ans.append(e)
while op:
    ans.append(op.pop())
print(''.join(ans))
