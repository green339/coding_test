# https://www.acmicpc.net/problem/20187
import sys
input=sys.stdin.readline

k=int(input())
n=2**k-1
min_x=0
min_y=0
max_x=n
max_y=n
cmd=list(input().strip().split())
for c in cmd:
    if c=="D":
        min_x=(max_x+min_x)//2+1
    elif c=="U":
        max_x=(max_x+min_x)//2
    elif c=="R":
        min_y=(max_y+min_y)//2+1
    elif c=="L":
        max_y=(max_y+min_y)//2
x=min_x%2
y=min_y%2
num=int(input())
row=[1,0,3,2]
col=[2,3,0,1]
if x==0 and y==0:
    shape=[[num,row[num]],[col[num],row[col[num]]]]
elif x==0 and y==1:
    shape=[[row[num],num],[row[col[num]],col[num]]]
elif x==1 and y==0:
    shape=[[col[num],row[col[num]]],[num,row[num]]]
elif x==1 and y==1:
    shape=[[row[col[num]],col[num]],[row[num],num]]
for i in range(n+1):
    tmp=[]
    for j in range(n+1):
        tmp.append(shape[i%2][j%2])
    print(*tmp)