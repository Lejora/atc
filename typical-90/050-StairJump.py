# 1段かL段
# N // L = S
# for s in range(S)
# if s == 1: rem = N - s * L
# 
# if s == 1 and rem == 14: 
#   combination = 15! / 1! * 14!

# s = 0
# 4! / 0! * (4-0*L)! = 1
# s = 1
# 1! / 1! * (4-1*L)! = 1


# 1st
# import math


# N, L = map(int, input().split())

# num_big_steps = N // L

# combs = []

# for s in range(num_big_steps + 1):
#   combination = int(math.factorial(s + (N - s * L)) \
#     / (math.factorial(s) * math.factorial(N - s * L)))
#   combs.append(combination)
#   # print(f"s: {s}, combs: {combs}")
  
# ans = int(sum(combs) % (10**9 + 7))
  
# print(ans)

N, L = map(int, input().split())
MOD = 10**9 + 7

step_arr = [0] * (N + 1)
step_arr[0] = 1
step_arr[1] = 1

for i in range(2, N + 1):
  # i - 1 段目にたどり着く通り
  before_mini_step = step_arr[i - 1]

  # i - L 段目にたどり着く通り
  if (i - L >= 0): 
    before_big_step = step_arr[i - L]
  else:
    before_big_step = 0
  
  step_arr[i] = before_big_step + before_mini_step
  
  # print(step_arr)
  
ans = step_arr[N] % (MOD)

print(ans)