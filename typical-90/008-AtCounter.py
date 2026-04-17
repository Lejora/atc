# attcordeer
# a(0)
# a(0) t(1) / t(2)
# a(0) t(1) / t(2) c(3) o(4) d(5) e(7) / e(8)
# a(0) t(1) / t(2) c(3) o(4) d(5) e(7) / e(8) r(9)
# 
# 
# ex1)
# a = [0]
# t = [1, 2]
# c = [3]
# o = [4]
# d = [5]
# e = [7, 8]
# r = [9]
# 

MOD = pow(10, 9) + 7
N = int(input())
S = input()
target = "atcoder"
dp = [0] * (len(target) + 1)
dp[0] = 1

# for char in S:
#   if char == "a":
#     dp[1] += dp[0]
#   elif char == "t":
#     dp[2] += dp[1]

for char in S:
  for j in range(len(target)):
    if char == target[j]:
      dp[j+1] = (dp[j+1] + dp[j]) % MOD
      
print(dp[7])