def solution(data, ext, val_ext, sort_by):
	int(input())
	di = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
	arr = []
	for i in data:
		if i[di[ext]] < val_ext:
			arr.append(i)
	return sorted(arr, key=lambda x : x[di[sort_by]])

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))

