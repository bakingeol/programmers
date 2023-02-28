def solution(a,b,n):
    result = 0
    x,y = 0,0
    while n >= a:
        x = (n//a)*b
        y = n-(n//a)*a
        n = x+y
        result += x
        
    return result