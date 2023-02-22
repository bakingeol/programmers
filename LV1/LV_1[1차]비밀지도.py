def solution(n, arr1, arr2):

    result = []
    for i,j in zip(arr1, arr2):
        
        i = '0'*(n-len(bin(i)[2:])) + bin(i)[2:]
        j = '0'*(n-len(bin(j)[2:])) + bin(j)[2:]

        x = ''
        for a1,a2 in zip(i, j):
            
            if int(a1)+int(a2) != 0:
                x += '#'
            else:
                x += ' '
        
        result.append(x)
    return result

# 다른사람 풀이 -------------------------------------------

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer