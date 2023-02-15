def solution(d, budget):
    x = 0
    z = []
    while x<=budget:
        try:
            y = min(d)
            d.remove(y)
            x += y
            if x > budget:
                break
            else:
                z.append(str(y))
        except ValueError:
            break
    return len(z)

# 다른사람 풀이-------------------------------
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
        
    return len(d)
