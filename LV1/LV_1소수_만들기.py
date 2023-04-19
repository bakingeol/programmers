from itertools import combinations
def solution(nums):
    count2 = 0
    x = list(combinations(nums,3))
    y = []
    
    for i in x:
        y.append(sum(i))
    
    leng = [True for i in range(max(y)+1)]
        
    for i in range(2, int(max(y)**0.5)+1):
        count = 2
        while i*count <= max(y):
            leng[i * count] = False
            count += 1
    
    for i in y:
        if leng[i] == True:
            count2 += 1
    
    return count2