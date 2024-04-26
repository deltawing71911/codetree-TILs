inp = input()
arr = inp.split()
h = int(arr[0])
w = int(arr[1])
b = int((100 * 100 * w) / (h * h))

print(b)
if int(b) >= 25:
    print("Obesity")