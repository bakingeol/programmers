def solution(answers):
    result = []
    num0 = [1, 2, 3, 4, 5]  #5
    num1 = [2, 1, 2, 3, 2, 4, 2, 5] #8
    num2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #10

    score = [0,0,0]

    for i,j in enumerate(answers):
        if num0[i%5] ==j:
            score[0] +=1
        if num1[i%8] ==j:
            score[1] +=1
        if num2[i%10] ==j:
            score[2] +=1
    
    for i in range(len(score)):
        if max(score) == score[i]:
            result.append(i+1)
    
    return result