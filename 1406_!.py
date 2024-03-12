# import sys

# N = list(sys.stdin.readline().strip())
# T = int(sys.stdin.readline().strip())
# cursor = len(N)

# for _ in range(T):
#     a = sys.stdin.readline().split()
#     if a[0] == "P":
#         N.insert(cursor, a[1])
#         cursor += 1
#     elif a[0] == "L":
#         if cursor != 0:
#             cursor -= 1
#     elif a[0] == "D":
#         if cursor != len(N):
#             cursor += 1
#     elif a[0] == "B":
#         if cursor != 0:
#             cursor -= 1
#             del N [cursor]

#     print(''.join(N))

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
	command = list(sys.stdin.readline().split())
	if command[0] == 'L':
		if st1:
			st2.append(st1.pop())
			
	elif command[0] == 'D':
		if st2:
			st1.append(st2.pop())

	elif command[0] == 'B':
		if st1:
			st1.pop()
			
	else:
		st1.append(command[1])
		
st1.extend(reversed(st2))
print(''.join(st1))