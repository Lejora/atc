S = input()

S_rev = S[::-1]
words = ["dream", "dreamer", "erase", "eraser"]
words_rev = [w[::-1] for w in words]

pointer = 0
is_ok = True

while pointer < len(S_rev):
  found = False
  for w in words_rev:
    if S_rev.startswith(w, pointer):
      pointer += len(w)
      found = True
      break

  if not found:
    is_ok = False
    break

if is_ok:
  print("YES")
else:
  print("NO")

# 文字を逆順にすると、接尾に左右されない特異な文字列になる
# S = input()

# def check_startswith_rule(sentence: str, pointer: int):
#   if sentence.startswith("eraser", pointer):
#     pointer += 6
#     return True, pointer
#   elif sentence.startswith("dream", pointer):
#     pointer += 5
#     return True, pointer
#   elif sentence.startswith("dreamer", pointer):
#     pointer += 6
#     return True, pointer
#   elif sentence.startswith("erase", pointer):
#     pointer += 5
#     return True, pointer
#   else:
#     return False, pointer
  
# pointer = 0

# is_ok = True

# while pointer < len(S):
#   is_ok, pointer = check_startswith_rule(sentence=S, pointer=pointer)
#   print(f"is_ok: {is_ok}, pointer: {pointer}")
#   pointer = pointer
#   if not is_ok:
#     break


# if is_ok:
#   print("YES")
# else:
#   print("NO")