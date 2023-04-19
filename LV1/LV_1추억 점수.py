def solution(name, yearning, photo):
    y = {}
    for i in range(len(name)):
        if name[i] not in y:
            y[name[i]] = yearning[i]
    
    result = []
    for i in photo:
        count = 0
        for j in i:
            if j in y:
                count += y[j]
            else:
                pass
        result.append(count)
            
    return result
