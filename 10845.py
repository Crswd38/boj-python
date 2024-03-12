import sys

N = int(sys.stdin.readline())   
queue = []

for i in range(N):
    A = sys.stdin.readline().split()
    if A[0] == "push":
        queue.append(A[1])
    elif A[0] == "pop":
        if len(queue) == 0:
            print(queue[0])
            del queue [0]

    elif A[0] == "size":
        if len(queue) == 0:
            print(0)
        else:
            print(len(queue))
    elif A[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif A[0] == "front":
        if len(queue) == 0:
            print(A[0])
    elif A[0] == "back":
        if len(queue) == 0:
            print(queue[len(queue)-1])