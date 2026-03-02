H, W = map(int, input().split(" "))

A = [list(map(int, input().split(" "))) for _ in range(H)]

row_sum = [sum(row) for row in A]

col_sum = [0 for _ in range(W)]

for i in range(H):
  for j in range(W):
    col_sum[j] += A[i][j]

for i in range(H):
  ans_row = []
  for j in range(W):
    res = row_sum[i] + col_sum[j] - A[i][j]
    ans_row.append(res)

  print(*(ans_row))
