# 不便さが変わるのはLとRの境界値だけ？
# inconv = [0] * (N-1)
# inconv[i] = [|A_i - A_(i+1)|]
# for q in range(Q)
#   inconv[L-1] -= V
#   inconv[R] += V
# ans = sum(inconv)

N, Q = map(int, input().split())

inconv = [0] * (N-1)

A = list(map(int, input().split()))


for i in range(N-1):
  # print(f"i: {i}, inconv[i]: {inconv[i]}, A[i-1]: {A[i-1]}, A[i]: {A[i]}")
  inconv[i] = A[i+1] - A[i]

ans = sum(abs(x) for x in inconv)  

for q in range(Q):
    L, R, V = map(int, input().split())
    
    # --- 左側の境界 (L) の更新 ---
    # 区画 L 以降が変わるので、inconv[L-1] が影響を受ける
    # L=1 のときは左側に隣がないのでスキップ
    if L > 1:
      ans -= abs(inconv[L-2])   # 変わる前の不便さを引く
      inconv[L-2] += V          # 差を更新
      ans += abs(inconv[L-2])   # 変わった後の不便さを足す
    
    # --- 右側の境界 (R) の更新 ---
    # 区画 R までが変わるので、inconv[R] が影響を受ける
    # R=N のときは右側に隣がないのでスキップ
    if R < N:
      ans -= abs(inconv[R-1])     # 変わる前の不便さを引く
      inconv[R-1] -= V            # 差を更新（右端は V 引かれる）
      ans += abs(inconv[R-1])     # 変わった後の不便さを足す

    print(ans)