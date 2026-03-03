N = int(input())

sum1 = [0] * (N+1)
sum2 = [0] * (N+1)

for i in range(N):
  cls, score = map(int, input().split(" "))
  
  sum1[i+1] = sum1[i]
  sum2[i+1] = sum2[i]
  
  if cls == 1:
    sum1[i+1] += score
  else:
    sum2[i+1] += score
    
Q = int(input())

results = []
for _ in range(Q):
  L, R = map(int, input().split(" "))
  
  ans1 = sum1[R] - sum1[L-1]
  ans2 = sum2[R] - sum2[L-1]
  
  results.append(f"{ans1} {ans2}")
  
  
print("\n".join(results))
  
# import sys

# input = sys.stdin.readline

# N = int(input())

# data = [list(map(int, input().split(" "))) for _ in range(N)]

# Q = int(input())

# point_range = [list(map(int, input().split(" "))) for _ in range(Q)]

# for r in point_range:
#     start = r[0]
#     stop = r[1]
#     p_class_1 = 0
#     p_class_2 = 0
    
#     for i in range(start-1, stop):
#         if data[i][0] == 1:
#             p_class_1 += data[i][1]
        
#         elif data[i][0] == 2:
#             p_class_2 += data[i][1]

#     print(f"{p_class_1} {p_class_2}")