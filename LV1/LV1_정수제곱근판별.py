def solution(n):
    x = n**0.5
    
    if (x*10)%10 == 0:
        return int((x+1)**2)
    else:
        return -1

'''
제곱근 씌운 후 if문을 통한 판별
'''

# -------------------------- 다른 사람 풀이
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
'''
1로 나머지 구하는 방법으로도 판별할 수 있음.
'''