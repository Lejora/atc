N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# A, B, Cそれぞれで46で割ったあまりを出す
# 要素数Nを0~45までハッシュ的に圧縮できる
# 各あまりの個数を各数列で計算しておくA'[] B'[] C'[]
# A' + B' + C' = 46になるあまりペア 
# ex) tuple(1, 26, 19) -> A'[1] * B'[26] * C'[19] = この組み合わせの個数

rem_a = [a % 46 for a in A]
rem_b = [b % 46 for b in B]
rem_c = [c % 46 for c in C]

rem_a_count = [0] * 46
rem_b_count = [0] * 46
rem_c_count = [0] * 46

for a in rem_a: rem_a_count[a] += 1
for b in rem_b: rem_b_count[b] += 1
for c in rem_c:rem_c_count[c] += 1

ans = 0

for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a + b + c) % 46 == 0:
                ans += rem_a_count[a] * rem_b_count[b] *rem_c_count[c]
                
print(ans)