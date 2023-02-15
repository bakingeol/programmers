def solution(s):
    answer = ''
    count = 0
    for i in s:
        if i == ' ':
            count = 0
            answer += ' '
            pass
        elif count/2 == count//2:
            answer += i.upper()
            count += 1
        else:
            answer += i.lower()
            count += 1

    return answer

'''
solution:
count로 갯수를 세다가 ' ' 을 만나면 count = 0으로 만들고 
짝홀수를 판단 후 upper lower을 결정해준다.
'''