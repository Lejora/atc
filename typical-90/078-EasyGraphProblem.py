import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))

nodes = [0 for _ in range(N+1)]

for m in range(M):
  a, b = map(int, input().split(" "))
  
  if a > b:
    nodes[a] += 1
  elif b > a:
    nodes[b] += 1
    
count = 0

for n in nodes:
  if n == 1:
    count += 1
    
print(count)