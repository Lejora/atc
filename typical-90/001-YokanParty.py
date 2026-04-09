N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def check(M):
  count = 0
  pre_cut_pos = 0
  
  for i in range(N):
    if A[i] - pre_cut_pos >= M:
      count += 1
      pre_cut_pos = A[i]
      
    if count == K:
      break
      
  if L - pre_cut_pos >= M and count == K:
    return True
  else:
    return False
    
left = -1
right = L + 1

while right - left > 1:
  mid = (left + right) // 2
  # score = [0, ..., L] から最大の M を見つける
  if check(mid):
    left = mid
  else:
    right = mid
    
print(left)