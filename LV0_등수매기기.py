score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
dict, average = {}, [sum(i)/len(i) for i in score]

for index, avg in enumerate(sorted(average, reverse = True), start = 1):
	if avg not in dict:
		dict[avg] = index
print([dict[i] for i in average])

'''solution
딕셔너리와 enumerate index를 활용한 정렬방식 사용
'''