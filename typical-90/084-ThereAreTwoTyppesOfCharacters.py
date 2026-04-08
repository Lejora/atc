N = int(input())
S = list(input())

count = 0

# for l in range(N):
#   for r in range(l, N):
#     if  "o" in S[l:r + 1] and "x" in S[l:r + 1]:
#       count += 1
    
#     last_seen_round_idx = r
      
# print(count)

last_o = -1
last_x = -1

# 4 ooxo
for r in range(N):
  if S[r] == "o":
    last_o = r # last_o = 1
  elif S[r] == "x":
    last_x = r # last_x = 2

  if last_o != -1 and last_x != -1:
    # 右端を固定したまま、左端をどこに置けば「"o"と"x"両方含まれるか」
    # oxxo min_x = 2, min_x + 1 = 3 (xo, xxo, oxxo)
    count += min(last_o, last_x) + 1
    
print(count)