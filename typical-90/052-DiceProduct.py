# 2
# 1 2 3 5 7 11
# 4 6 8 9 10 12
# 
# 1*4 + 1*6 + ... = 1 * (4 + 6 + ...)
# 
# 

MOD = 10**9 + 7

N = int(input())

res = 1

for n in range(N):
  row_sum = sum(
    list(map(int, input().split()))
  )
  
  res *= row_sum
  
print(res % MOD)