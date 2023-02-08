def solution(a_1):
    x = []

    for row, row_val in enumerate(a_1):
        for col, col_val in enumerate(a_1[row]):
            if a_1[row][col] == 1:
                x.append([row, col]) 

    for i in x:
        row, col = i[0], i[1]
        for j in range(-1,2,1):
            for k in range(-1,2,1):
                if len(a_1)-1 >= row + j >= 0 and len(a_1[0])-1 >= col + k >= 0:
                    a_1[row + j][col + k] = 1
                else:
                    pass

    count = 0
    for i in a_1:
        count += i.count(0)
        
    return count
'''
solution :
첫 번째 for문에서는 기존 2차원 행렬에서 1을 찾아내는 과정을 진행
두 번째 for문에서는 -1, 0, 1을 더해 기존 행렬을 바꿔준다 
세 번째 for문에서는 0 숫자 카운트
'''