def solution(common):
    
    if common[2] - common[1] == common[1] - common[0]:
        return common[-1] + common[-1] - common[-2]
    elif common[2] / common[1] == common[1] / common[0]:
        return common[-1] * (common[-1] / common[-2])
'''
solution : 등차, 등비 수열 수식 생각해서 다음 나올 수 리턴
'''