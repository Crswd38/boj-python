def solution(intStrs, k, s, l):
    result = []
    for i in intStrs:
        i = str(i)
        if int(i[s:s+l]) > k:
            result.append(int(i[s:s+l]))
    return result

print(solution(["0123456789","9876543210","9999999999999"],50000,5,5))