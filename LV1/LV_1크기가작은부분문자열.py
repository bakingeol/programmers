def solution(t, p):
    a = []
    for i in range(len(t)-len(p)+1):
        a.append(t[i:i+len(p)])

    count = 0
    for j in a:
        if int(j) <= int(p):
            count += 1
            
    else:
        return count