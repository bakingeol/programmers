def solution(a):
    a = a.split(' ')
    count = []
    count2 = 0
    counts = 0
    for i,j in enumerate(a):
        if 'x' in j:
            j = list(j)
            del j[-1]
            if ''.join(j) == '':
                j = '1'
            count.append(''.join(j))   
        elif j.isdigit() == True:
            count2 += int(j)

    counts = sum(map(int, count))

    if count2 != 0 and counts ==0:
        return ''.join([str(count2)])    
    elif count2 != 0 and counts != 0:
        if counts == 1:
            return ''.join(['x',' ','+',' ',str(count2)])
        return ''.join([str(counts),'x',' ','+',' ',str(count2)])
    elif count2 == 0 and counts != 0:
        if counts == 1:
            return ''.join(['x'])
        return ''.join([str(counts),'x'])
    elif count2 ==0 and counts ==0:
        return ''
    
'''
solution : x값과 상수항을 나눠서 count로 더하는 방식으로 진행한 후 마지막에는 경우에 따라 return 해주었습니다.
ps. 마지막 return 하는 과정에서 좀 더럽게 푼 것 같습니다....
'''