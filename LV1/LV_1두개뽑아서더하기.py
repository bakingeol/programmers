def solution(numbers):
    x = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            x.append(numbers[i]+numbers[j])
    return sorted(set(x), reverse=False)