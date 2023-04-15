def solution(n):
    count = 0
    array = [True for i in range(0,n+1)]
    
    for i in range(2, int(n**0.5)+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
    
    for i in array[2:]:
        if i == True:
            count+=1
    
    return count
