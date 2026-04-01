def solve():
  MOD = pow(10, 9) + 7
  N, K = map(int, input().split())
  
  if K == 1:
    return 1 if N == 1 else 0
  if K == 2:
    if N == 1 or N == 2: return 2
    return 0
  
  if N == 1:
    ans = K
  elif N == 2:
    ans = K * (K - 1)
  else:    
    num_pow = N - 2
    ans = (K % MOD) * (K - 1)  * pow(K - 2, num_pow, MOD)
    
  return ans % MOD

print(solve())