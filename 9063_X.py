import sys

a = int(sys.stdin.readline().strip())
x = []
y = []

for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    x.append(b)
    y.append(c)

print(max(x)*max(y))