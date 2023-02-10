def solution(arr):
    suma = sum(list(map(int,str(arr))))
    if arr // suma == arr/suma:
        return True
    else:
        return False
    
'''
solution:
정수 -> str -> list -> 합을 구한다 -> 나누어 떨어지는지 검증
'''