def solve1():
  N  = int(input())

  if N % 2 != 0:
    return
  
  for i in range(1 << N):
    candidate = ""
    
    for j in range(N - 1, -1, -1):
      if (i >> j) & 1:
        candidate += ")" # 1なら')'
      else:
        candidate += "(" # 0なら'('
    
    score = 0
    is_ok = True
    for char in candidate:
      if char == "(":
        score += 1
      else:
        score -= 1
        
      # 途中で"("の数よりも")"が多くなってはダメ
      if score < 0:
        is_ok = False
        break
    
    if is_ok and score == 0:
      print(candidate)

solve1()

def solve2():
    N = int(input())
    if N % 2 != 0:
        return

    # current: 今作っている文字列
    # open_count: 使った '(' の数
    # close_count: 使った ')' の数
    def dfs(current, open_count, close_count):
        # 1. 【終了条件】長さが N になったら完成！
        if len(current) == N:
            print(current)
            return

        # 2. 次の1文字をどうするか？
        # '(' を足せるかチェック（辞書順なので '(' を先に試す）
        if open_count < N // 2:
            dfs(current + "(", open_count + 1, close_count)
        
        # ')' を足せるかチェック
        if close_count < open_count:
            dfs(current + ")", open_count, close_count + 1)

    # 最初は空っぽの状態からスタート
    dfs("", 0, 0)

solve2()


# def add_pars(valid_pars: str):
#   return "(" + valid_pars + ")"

# def solve():
#   N = int(input())
#   patterns = set()
  
#   if N % 2 != 0: 
#     return patterns

#   center = "()"
#   left = ""
#   right = ""
#   length = 2
  
#   while length < N:
#     pattern = add_pars(left) + add_pars(center) + add_pars(right)
#     length = len(pattern)
#     patterns.add(pattern)
    
#   return patterns
      
# patterns = solve()

# print(pattern for pattern in patterns)