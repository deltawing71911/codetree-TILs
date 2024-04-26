inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

maxnum = a if a > b else b

print(maxnum)