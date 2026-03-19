import itertools


N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

M = int(input())

bad = [[False] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    
    u -= 1
    v -= 1
    
    bad[u][v] = True
    bad[v][u] = True
    
ans = float("inf")

# perm = (1, 0, 2) -> perm[0] = 1 (第0区間は選手1が走る)
for perm in itertools.permutations(range(N)):
    for i in range(N-1):
        if bad[perm[i]][perm[i+1]] == True:
            break
    else:
        time = 0
        
        for i in range(N):
            # A[走者][区間]
            time += A[perm[i]][i]
            
        ans = min(ans, time)
            
if ans != float("inf"):
    print(ans)
else:
    print(-1)
    
# hard