def solution(num_list):
    odd = []
    even = []
    for i in num_list:
        if i % 2 == 0:
            odd.append(str(i))
        else:
            even.append(str(i))
    return int(''.join(odd)) + int(''.join(even))

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))