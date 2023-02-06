def solution(quiz):
    a = []
    for i in quiz:
        i = i.split('=')

        if eval(i[0]) == int(i[-1]):
            a.append('O')
        else:
            a.append('X')
    return a
'''
solution : for문을 통해 받은 str 형태를 split으로 나눈 후 eval함수를 사용해 str형태의 문장 연산
'''