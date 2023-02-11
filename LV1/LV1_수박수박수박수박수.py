def solution(n):
    a = []
    for i in range(n):
        if i//2 == i/2:
            a.append('수')
        elif i//2 != i/2:
            a.append('박')
    return ''.join(a)