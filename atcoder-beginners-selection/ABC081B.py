N = int(input())
arr = list(map(int, input().split(" ")))

count = 0

while True:
  can_divide = True

  for x in arr:
    if x % 2 != 0:
      can_divide = False
      break

  if not can_divide:
    break

  arr = [x // 2 for x in arr]
  count += 1

print(count)