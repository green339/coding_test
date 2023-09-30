def rotate(arr):
    res=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[i][j]=arr[N-1-j][i]
    return res
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    board=[list(map(str,input().strip().split())) for _ in range(N)]
    rotate_90=rotate(board)
    rotate_180=rotate(rotate_90)
    rotate_270=rotate(rotate_180)
    print(f'#{tc}')
    for i in range(N):
        print(''.join(rotate_90[i]),end=" ")
        print(''.join(rotate_180[i]),end=" ")
        print(''.join(rotate_270[i]), end=" ")
        print()