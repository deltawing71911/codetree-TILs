phone = input()
arr = phone.split("-")

front = arr[1]
back = arr[2]
print(f"010-{back}-{front}")