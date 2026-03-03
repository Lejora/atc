import sys

input = sys.stdin.readline

N, P, Q = map(int, input().split(" "))

A = [x % P for x in list(map(int, input().split(" ")))]

count = 0

for i in range(N):
  for j in range(i + 1, N):
    v2 = A[i] * A[j] % P
    for k in range(j + 1, N):
      v3 = v2 * A[k] % P
      for l in range(k + 1, N):
        v4 = v3 * A[l] % P
        for m in range(l + 1, N):
          v5 = v4 * A[m] % P
          if v5 == Q:
            count += 1

print(count)