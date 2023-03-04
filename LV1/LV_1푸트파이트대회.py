def solution(food):
    x = ''
    for index, value in enumerate(food):
        if index == 0:
            pass
        x += f'{index}'*(value//2)
    
    return x + '0' + x[::-1]