# gcd(a, b) * lcm(a, b) = a * b

A, B = map(int, input().split())

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def solve():
  lcm = A * B // gcd(A, B)
  
  if lcm > 10**18:
    print("Large")
  else:
    print(lcm)
    
solve()