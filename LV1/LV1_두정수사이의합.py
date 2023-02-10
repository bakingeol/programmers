def solution(a, b):
    x, y = min([a,b]), max([a,b])
    a = []
    for i in range(0,y-x+1):
        if x<=x+i<=y:
            a.append(x+i)

    return sum(set(a))

'''
solution:
min, max 값을 구한 후 리스트에 추가하는 방식.
'''

# 다른 풀이 방식-----------------------------------------
def adder(a, b):
    if a > b: a, b = b, a

    return sum(range(a,b+1))

'''
for 문을 돌릴 필요 없이 range 문장을 끝낼 수 있다..
'''