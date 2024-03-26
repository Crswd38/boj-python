import sys

N = int(sys.stdin.readline())
result = ''

while N != 0:
    remainder = N % 2
    N = -(N // 2)
    if remainder < 0:
        remainder += 2
        N += 1
    result = str(remainder) + result
print(result)