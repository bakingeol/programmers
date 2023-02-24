def solution(array, commands):
    
    result = []
    for i in commands:
        result.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    
    return result

