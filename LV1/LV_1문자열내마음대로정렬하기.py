def solution(strings, n):
    x = {}
    for i in strings:
        if i not in x:
            x[i] = i[n]
    y = sorted(sorted(strings), key = x.__getitem__)
    return y

'''
solution:
strings를 정렬된 산태에서 dictionary x 의 value를 뽑아낸 값을 기준으로 다시 정렬
'''