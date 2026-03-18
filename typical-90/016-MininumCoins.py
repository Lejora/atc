N = int(input())

A, B, C = map(int, sorted(input().split(), reverse=True))

# A*x + B*y + C*z = N
# x + y + z < 10000

MAX_COINS = 10000


def solve():
  ans = 10000000000
  
  for x in range(MAX_COINS):
    a_sum = A * x
    if a_sum > N: 
      break
    
    for y in range(MAX_COINS - x):
      b_sum = B * y
      c_sum = N - (a_sum + b_sum)
      
      if c_sum < 0:
        break
      
      if c_sum % C == 0:
        z = c_sum // C
        # print(f"x: {x} y:{y} z:{z}")
        # print(f"a_sum: {a_sum} b_sum:{b_sum} c_sum:{c_sum}")
        candidate = x + y + z
        if candidate < 10000 and ans > candidate:
          ans = candidate
  
  return ans

print(solve())