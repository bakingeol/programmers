def solution(arr):
    arr.remove(min(arr))
    if arr == []:
        return [-1]
    else:
        return arr

'''
solution:
remove함수를 이용해 가장 작은 수 제거
'''