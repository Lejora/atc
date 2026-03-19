#     z
#     |
#     |
#     |
#     *--------- x
#    /
#   /
#  /
# y
#
#     z
#    T/2  
#     |  T/4
#3T/4 |
#     0--------- x
#    /
#   /
#  /
# y

import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]


def angle(height, distance):
  if height >= 0 and distance >= 0:
    return math.degrees(math.atan2(height, distance))

for e in E:
  theta = 2 * math.pi * e / T

  look_x = 0
  look_y = -L/2 * math.sin(theta)
  look_z = L/2 - L/2 * math.cos(theta)
    
  height = abs(look_z)
  distance = math.sqrt((X - look_x)**2 + (Y - look_y)**2)
  
  result = angle(height, distance)
  
  print(result)
