def solution(left, right):
    result = 0
    
    for i in range(left,right+1):
        count = 0
        for j in range(1,i+1):
            if i//j == i/j:
                count += 1
        if count%2 == 0:
            result += i
        elif count%2 == 1:
            result -= i
    
    return result

'''
solution:
left와 right의 숫자를 i에 하나 씩 돌아가게 하고, j와 i가 나눠떨어지면 count를 더해준다.
이때 짝수개면 reuslt에 i를 더해주고 홀수면 result에 j를 더해준다.
'''