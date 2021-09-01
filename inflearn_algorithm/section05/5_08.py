import sys

N=int(sys.stdin.readline())
words=dict()
for _ in range(N):
    words[sys.stdin.readline().strip()]=1

for _ in range(N-1):
    words[sys.stdin.readline().strip()]-=1

for k,v in words.items():
    if v:
        print(k)
        break
