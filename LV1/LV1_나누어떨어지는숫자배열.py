def solution(arr, divisor):
    answer = []
    for i in arr:
        if i//divisor == i/divisor:
            answer.append(i)
    if answer == []:
        return [-1]
    else:
        return sorted(answer)

'''
solution:
나눠떨어지는수를 append, 만약 공백일때는 return [-1]
공백이 아닐 때 정렬 후 return
'''