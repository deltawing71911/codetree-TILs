inp = input()
arr = inp.split()
a_math = int(arr[0])
a_eng = int(arr[1])

inp = input()
b_math = int(arr[0])
b_eng = int(arr[1])

if a_math > b_math or (a_math == b_math and a_eng > b_eng):
    print("A")
else:
    print("B")