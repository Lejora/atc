import sys

input = sys.stdin.readline

def dec_to_base_n(num, base) -> str:
  if num == 0:
    return '0'
  
  str_n = ''
  while num:
    str_n += str(num % base)
    num //= base
  return str_n[::-1]

data = input().split(" ")
# Nは8進数
N_str = data[0]
K = int(data[1])

for i in range(K):
  # base 8 -> 10
  dec = int(N_str, 8)
  
  # base 10 -> 9
  nona = dec_to_base_n(dec, 9)
  
  N_str = nona.replace('8', '5')
  
print(N_str)