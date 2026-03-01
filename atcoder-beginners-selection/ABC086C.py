N = int(input())

rules = []

for i in range(N):
  rules.append(list(map(int, input().split(" "))))

def check():
  current_t = 0
  current_pos_x = 0
  current_pos_y = 0

  for t, x, y in rules:
    dist = abs(x - current_pos_x) + abs(y - current_pos_y)
    dt = t - current_t

    if dt < dist or (dt - dist) % 2 != 0:
      return False
    
    current_t = t
    current_pos_x = x
    current_pos_y = y

  return True

if check():
  print("Yes")
else:
  print("No")