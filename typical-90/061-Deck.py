Q = int(input())

box = []
paper = []

for i in range(Q):
  t, x = map(int, input().split(" "))
  
  if t == 1:
    box.insert(0, x)
    
  elif t == 2:
    box.append(x)
    
  elif t == 3:
    write_num = box[x-1]
    paper.append(write_num)
    
for num in paper:
  print(num)
  
# deque is faster

from collections import deque
import sys

input = sys.stdin.read
Q = int(input())
data = input().split()

box = deque()
paper = []

idx = 1
for _ in range(Q):
  t = int(data[idx])
  x = int(data[idx+1])
  idx += 2
  
  if t == 1:
    box.appendleft(x) # fast
  elif t == 2:
    box.append(x)
  elif t == 3:
    paper.append(box[x-1])
    
print("\n".join(map(str, paper)))