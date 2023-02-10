def solution(n):
    count = 0
    while n != 1:

        if n / 2 == n//2:
            n = n/2
        else:
            n = n * 3 + 1
        count += 1
        if count > 500:
            return -1
    return count
'''
solution:
n = 1이 될때 가지 반복하면서 count가 500이 넘어가는지 확인
500이내에 통과하면 count를 반환
'''