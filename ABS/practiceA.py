input1 = input()
input2 = input()
input3 = input()
bcArr = input2.split(" ")
bcArrLen = len(bcArr)

a = int(input1)
b = int(bcArr[0])
c = int(bcArr[bcArrLen - 1])
s = str(input3)

print(f"{a+b+c} {s}")
