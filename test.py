def solution(numLog):
    d = {1:"w", -1:"s", 10:"d", -10:"a"}
    result = []
    last = 0
    cnt = 0
    for i in numLog[1:]:
        result.append(d[i - last])
        last = i
    return ''.join(result)

print(solution([-1, 0]))