def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 다른 사람 풀이 ------------------------------------
def solution(arr):
    stack = []
    result = [arr[0]]
    for num in arr:
        if stack:
            curr = stack.pop()
            if curr != num:
                result.append(num)

        stack.append(num)
    return result