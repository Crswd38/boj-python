def solution(s):
    result = ""
    for i in s.split():
        for j in range(len(i)):
            if j%2:
                result += i[j].lower()
            else:
                result += i[j].upper()
        result += " "
    return result



print(solution("  TRy HElLo  WORLD "))
# print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
# print(solution([[1, 2], [3, 4]]))