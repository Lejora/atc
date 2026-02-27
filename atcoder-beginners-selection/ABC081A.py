field = int(input())

s1 = field // 100
s2 = (field - s1 * 100) // 10
s3 = field - s1 * 100 - s2 * 10

print(s1 + s2 + s3)