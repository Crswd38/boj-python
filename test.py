def solution(emergency):
    arr = sorted(emergency)
    result = []
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if emergency[i] == arr[j]:
                result.append(j)
    return ''.join(result)


print(solution([3, 76, 24]))
