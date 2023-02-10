def solution(num, total):
    if num % 2 == 1:
        mean_num = total / num
    elif num % 2 == 0:
        mean_num = int(total / num) + 1
    
    start_num = int(mean_num - int(num/2))
    return [i for i in range(start_num, start_num + num)]

'''
solution : 총 합 숫자와 숫자 갯수를 나눌때 result의 평균이 나온다. 
평균에서 시작 숫자를 구하기 위해 숫자 갯수를 반으로 나눈 것을 뺴준다. 
이후 list comprehension을 통해 리턴해준다.
'''