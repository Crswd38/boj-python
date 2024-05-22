n, m = map(int, input().split())
sum = n
for i in range(1, m):
    sum *= n
    print(str(sum)[-1])