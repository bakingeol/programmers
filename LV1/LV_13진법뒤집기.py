def solution(n):
    x = 0
    while n >= 3**x:
        x +=1

    a = []
    for i in range(x-1,-1,-1):
        j=0
        while n >= 3**i * j:
            j += 1
        j -= 1
        n -= 3**i * j
        a.append(str(j))

    b = a[::-1]

    result = 0
    for i in range(1, len(b)+1):
        result += int(b[-i]) * 3**(i-1)

    return result

# 다른 사람 풀이 --------------------------------------
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

'''
solution: 
내가 푼 방법은 3진법을 구하고 이걸 뒤집고 나서 10 진법으로 표현하는 방법
다른 사람 풀이는 앞뒤 반전된 3진법으로 바로 표현하고 이를 int함수를 이용해 쉽게 해결함...
'''