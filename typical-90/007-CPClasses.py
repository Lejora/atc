import sys
import bisect

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split(" ")))

A_sorted = sorted(A)
# print(A_sorted)

Q = int(input())

margin = []

for i in range(Q):
    B = int(input())
    
    insert_index = bisect.bisect(A_sorted, B)
    
    # print(insert_index)
    
    # Bが最小のAより小さいとき
    if insert_index == 0:
        margin.append(
            abs(B - A_sorted[0])
        )
    # Bが最大のAよりも大きいとき
    elif insert_index == N:
        margin.append(
            abs(B - A_sorted[N-1])
        )
    else:    
        margin.append(
            min(abs(B - A_sorted[insert_index-1]), abs(B - A_sorted[insert_index]))
        )
        
    
print(*margin, sep="\n")