inp = input()
arr = inp.split()
width = int(arr[0])
height = int(arr[1])

width += 8
height *= 3

print(width)
print(height)
print(width * height)