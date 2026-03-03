N = int(input())

d = {}

for i in range(N):
  user_name = input()
  
  if user_name not in d.keys():
    d[user_name] = i + 1

for v in d.values():
  print(v)
  

# import sys

# input = sys.stdin.readline

# N = int(input())
# seen_users = set()

# for i in range(1, N+1):
#   user_name = input().strip()
  
#   if user_name not in seen_users:
#     print(i)
#     seen_users.add(user_name)