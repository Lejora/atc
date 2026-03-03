import math

A, B, C = map(int, input().split(" "))

gcd = math.gcd(A, B, C)


cut_count = 0

if A % gcd == 0:
  cut_count += A // gcd - 1

if B % gcd == 0:
  cut_count += B // gcd - 1

if C % gcd == 0:
  cut_count += C // gcd - 1
  
print(cut_count)