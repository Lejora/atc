N, A, B = map(int, input().split())

count = 0

for i in range(1, N + 1):
  digit = map(int, str(i))
  digit_sum = 0
  for d in digit:
    digit_sum += d

  if A <= digit_sum <= B:
    count += i

print(count)