

def solution(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] / 2 if arr[i] >= 50 else arr[i] * 2
    return arr