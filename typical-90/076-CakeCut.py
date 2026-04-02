
# def solve():
#   N = int(input())
#   A = list(map(int, input().split()))
  
#   whole_size = sum(A)
  
#   if whole_size % 10 != 0:
#     return "No"
  
#   ten_split_size = whole_size // 10

#   for head_idx in range(N):
#     offset = 0
#     size = A[head_idx + offset]
    
#     if size == ten_split_size: return "Yes"
      
#     while size < ten_split_size:
#       offset += 1
#       idx = (head_idx + offset) % N
#       size += A[idx]      
      
#       if size == ten_split_size:
#         return "Yes"
      
#   return "No"

# print(solve())

def solve():
  N = int(input())
  A = list(map(int, input().split()))
  
  total_sum = sum(A)
  
  if total_sum % 10 != 0:
    return "No"
  
  target = total_sum // 10
  
  # ex) A = [0, 10] then, B = A + A = [0, 10, 0, 10]
  B = A + A
  
  right = 0
  current_sum = 0
  
  for left in range(N):
    # extend right until target
    while right < left + N and current_sum < target:
      current_sum += B[right]
      right += 1
      
    if current_sum == target:
      return "Yes"
    
    current_sum -= B[left]
    
  return "No"

print(solve())

# 円環が来たら2つ繋げて真っすぐにする！
# 連続する部分 -> 尺取り法　尺取り虫のように右端を伸ばしてから左端が追いかけてくる動き