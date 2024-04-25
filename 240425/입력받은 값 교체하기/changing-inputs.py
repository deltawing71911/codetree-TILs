inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

tmp = a
a = b
b = tmp

print(a, b)