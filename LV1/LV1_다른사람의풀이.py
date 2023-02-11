def solution(arr1, arr2):
    result = []
    
    for i in range(len(arr1)):
        x = []
        for j in range(len(arr1[0])):
            x.append(arr1[i][j] + arr2[i][j])
        result.append(x)
    
    return result

'''
solution:
행을 i, 열을 j로 지정하고 하나씩 대입해주는 방법
'''

# 다른사람 풀이 -------------------------------------------------
def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]

'''
solution:
zip을 이용해 두 list를 합쳐주고 zip(*x)를 이용해 합쳐진 것을 풀어준다. 맨 뒤 for문에서는 list가 앞에서 순차적으로 들어가고 
zip(*x) 부분에서는 map을 이용해 list의 합을 리스트로 만들어 준다 (각각) 그후 다시 리스트로 감싸기
'''