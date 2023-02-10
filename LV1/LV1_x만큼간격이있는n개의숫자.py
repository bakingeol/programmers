def solution(x, n):
    y = x
    b = []
    a = 1
    while a<=n:
        b.append(y)
        y += x
        a += 1
    return b