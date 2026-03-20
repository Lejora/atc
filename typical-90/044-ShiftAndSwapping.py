N, Q = map(int, input().split())

A = list(map(int, input().split()))

shift = 0

for q in range(Q):
  T, x, y = map(int, input().split())
  
  if T == 1:
    idx_x = (x - 1 - shift) % N
    idx_y = (y - 1 - shift) % N
    
    A[idx_x], A[idx_y] = A[idx_y], A[idx_x]
    
    # print(A)
  
  elif T == 2:
    shift += 1
    
    # print(A)
  
  elif T == 3:
    idx_x = (x - 1 - shift) % N
    print(A[idx_x])