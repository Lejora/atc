# def prime_fact(prime_number)
#   if prime_number <= 2
#     return prime_number
#   for n in range(2, prime_number)
#     if prime_number % n == 0
#       return n, prime_number // n
#     else
#       return prime_number
# 
# prime_list = [N]
# prev_len, cur_len = 1
# count = 0
# while prev_len < cur_len:
#   prev_len = cur_len
#   for n in prime_list
#     prime_list.append(prime_fact(n))
#   cur_len = len(prime_list)
#   count += 1


# def prime_fact(prime_number):
#   for n in range(2, prime_number):
#     if prime_number % n == 0:
#       return n, prime_number // n
#     else:
#       return prime_number
    
# def solve():
#   N = int(input())
#   prime_list = [N]
#   prev_len = 0
#   cur_len = 1
#   count = 0
  
#   while prev_len < cur_len:
#     prev_len = cur_len
#     for n in prime_list:
#       fact = prime_fact(n)
#       print(fact)
#       if isinstance(fact, tuple):
#         prime_list.append(fact[0])
#         prime_list.append(fact[1])
#     cur_len = len(prime_list)
#     count += 1
    
#   return count

# print(solve())

import math

def count_prime_factors(n): # 42
  count = 0
  d = 2
  temp = n # 42
  
  # 2 * 2 <= 42 自身(d)より大きい因数が存在するのはd**2 <= nの時
  while d * d <= temp:
    while temp % d == 0: # 42 % 2 == 0
      count += 1
      temp //= d # temp = 42 // 2 = 21
    d += 1
  if temp > 1: # 最後に残ってtempはそれ以上小さい数で割り切れなかった=素数
    count += 1
  return count

N = int(input())
K = count_prime_factors(N)
# K = 3 (2, 3, 7 when N == 42) 1回目で42 -> 2, 21 | 2回目で21 -> 3, 7
# 2**m >= Kを満たす最小の m が ans (1回目の魔法で因数2個、2回目の魔法で因数4個... 作れるため)
if K == 1:
  print(0)
else:
  ans = math.ceil(math.log2(K))
  print(ans)