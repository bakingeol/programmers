def solution(n):
    a = list(map(int,str(n)))
    return [a[-i] for i in range(1,len(a)+1)]

'''
solution:
map함수를 이용해 list형태 int형으로 만든 후 
list comprehension을 이용해 a[-i]부터 return
'''

#-------------------------- 다른사람풀이 
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

#-------------------------- 추가
def solution2(n):
    return list(map(int,str(n)))[::-1]
'''
for문을 사용할 필요가 없음
'''