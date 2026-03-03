N, Y = map(int, input().split(" "))

def solve():
  for i in range(N + 1):
    for j in range(N - i + 1):
      k = N - i - j
  
      if 10000 * i + 5000 * j + 1000 * k == Y:
        return f"{i} {j} {k}"
      
  return "-1 -1 -1"

print(solve())


# is_true = False
# err_num = -1

# for i in range(N + 1):
#   for j in range(N - i + 1):
#     for k in range(N - i - j + 1):
#       if i * 10000 + j * 5000 + k * 1000 == Y and i + j + k == N:
#         result = [i, j, k]
#         is_true = True
#         break

#     if is_true:
#       break

#   if is_true:
#     break

# if is_true:
#   print(f"{result[0]} {result[1]} {result[2]}")
# else:
#   print(f"{err_num} {err_num} {err_num}")