N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sorted = sorted(A)
B_sorted = sorted(B)

d = [0 for _ in range(N)]

for n in range(N):
    d[n] = abs(A_sorted[n] - B_sorted[n])
    
print(sum(d))