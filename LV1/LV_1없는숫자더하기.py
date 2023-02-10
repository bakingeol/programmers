def solution(numbers):
    count = 0
    for i in range(0,10):
        if i not in numbers:
            count += i
    return count