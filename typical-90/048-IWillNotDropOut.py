# -> 2min x point (満点) -> 1min x/2 point
# -> 1min y point (部分点)
#
# 
# A - B が+1分で得られる点数 
# 部分点の2倍は満点より大きい 2B > A 
# 部分点は満点から部分点を引いたものより大きい = B > A -B
# AとA-Bを配列にしてsort

N, K = map(int, input().split())

score = []

for i in range(N):
  A, B = map(int, input().split())
  C = A - B
  score.append(B)
  score.append(C)

score.sort(reverse=True)
  
ans = sum(score[:K])

print(ans)