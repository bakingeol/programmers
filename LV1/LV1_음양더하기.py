def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)

'''
solution:
signs에 음수면 -를 대입하는 식으로 작성
'''