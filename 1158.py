import sys

N, K = map(int, sys.stdin.readline(),splist())   
josephus = []
result = []
j = 0
cnt = 0

for i in range(N):
    josephus.append(i+1)

cnt = N
while(True):
    j += K
    if j > len(josephus)-1:
        j -= N
    else:
        result.append(josephus.pop(j))

    # 1 2 3 4 5 6 7     3 6 9-7
    # 1 2 4 5 7         2 5 8-5
    # 1 4 5             3 6-3
    # 1 4               3-2
    # 1 4               1 4-2
    # 4                 2-1
    # 4                 1