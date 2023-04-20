def solution(k, m, score):
    result = 0
    score = sorted(score,reverse = True)
    
    if len(score)<m:
        return 0
    
    for i in range(0,len(score)//m,1):
            
        result+=score[i*m+m-1]*m
        
    return result    