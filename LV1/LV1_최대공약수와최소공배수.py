def solution(n,m):
    n_li, m_li = [], []
    
    for i in range(1,n+1):
        if n/i == n//i:
            n_li.append(i)
    for i in range(1,m+1):
        if m/i == m//i:
            m_li.append(i)
    
    y = set(n_li + m_li) - (set(m_li) - set(n_li)) - (set(n_li)- set(m_li))
    y = sorted(list(y))
    
    result = []
    
    if len(y) == 1:
        result.append(y[0])
    else: 
        result.append(y[-1])
    
    result.append(int(n*m/result[0]))
    
    return result
'''
solution:
배열의 형태로 약수를 다 구한 후 집합의 형태로 표현해 공집합중 가장 큰 값을 공약수로 설정
공배수는 n*m/공약수
'''

# 다른사람 풀이 -----------------------------------------------
# gcd 유클리드 호제법 사용한 풀이

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))


def gcdlcm(a, b):
    answer = [gcd(a,b), lcm(a,b)]

    return answer