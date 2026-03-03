H, W = map(int, input().split(" "))

row_on = 0
column_on = 0

if H == 1 or W == 1:
  ans = H * W

else:

  row_on = (H + 1) // 2
  column_on = (W + 1) // 2

  ans = row_on * column_on

print(ans)