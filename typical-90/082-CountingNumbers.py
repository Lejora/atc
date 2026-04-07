MOD = pow(10, 9) + 7

L, R = map(int, input().split())

MAX_EXP = 18
total_length = 0

for exp in range(MAX_EXP + 1):
  L_digit = 10 ** exp
  R_digit = 10 ** (exp + 1) - 1
  
  # print(f"L_digit: {L_digit} R_digit: {R_digit}")
  # print(f"L: {L} R_digit: {R}")
  
  L_duplicate = max(L, L_digit)
  R_duplicate = min(R, R_digit)
    
  # print(f"L_dup: {L_duplicate} R_dup: {R_duplicate}")
  
  if L_duplicate <= R_duplicate:  
    len_digit = exp + 1
    # L_duplicate から R_duplicate までの「連続する整数の和」を求める 等差数列の和
    sum_x = (L_duplicate + R_duplicate) * (R_duplicate - L_duplicate + 1) // 2
    
    total_length += len_digit * sum_x
  
print(total_length % MOD)