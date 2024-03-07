N = 60466175
B = 36
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    s += str(arr[N%B])
    print(N%B)
    N //= B