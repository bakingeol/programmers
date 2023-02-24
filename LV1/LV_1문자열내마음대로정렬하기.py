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
# 더 간단한 방법
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])