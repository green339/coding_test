from collections import defaultdict,deque

def find(x):
    if visited[parent[x]] == 1:
        return parent[x]
    if parent[x] == x:
        return x
    visited[parent[x]] = 1
    return find(parent[x])


T = int(input())
for test_case in range(1, T + 1):
    V, E, one, two = map(int, input().split())
    tmp = list(map(int, input().split()))
    parent = [i for i in range(V + 1)]
    child=defaultdict(list)
    visited = [0] * (V + 1)
    for i in range(E):
        parent[tmp[2 * i + 1]] = tmp[2 * i]
        child[tmp[2*i]].append(tmp[2*i+1])
    find(one)
    common_parent=find(two)
    q=deque([common_parent])
    cnt=1
    while q:
        x=q.popleft()
        for nx in child[x]:
            cnt+=1
            q.append(nx)
    print(f'#{test_case} {common_parent} {cnt}')
