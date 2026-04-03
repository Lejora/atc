H, W = map(int, input().split())
  
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]


def calc():
  count = 0
  for y in range(H-1):
    for x in range(W-1):
      gap = B[y][x] - A[y][x]
      
      A[y][x] += gap
      A[y][x+1] += gap
      A[y+1][x] += gap
      A[y+1][x+1] += gap
      count += abs(gap)
      
      
  if A == B:
    return True, count
  else:
    return False, 0
    
can, count = calc()

if can:
  print("Yes")
  print(count)
else:
  print("No")