N = int(input())

d_arr = []

for i in range(N):
  d = int(input())
  d_arr.append(d)

d_arr.sort(reverse=True)

count = 1

for j in range(1, len(d_arr)):
  if d_arr[j] < d_arr[j-1]:
    count += 1

print(count)