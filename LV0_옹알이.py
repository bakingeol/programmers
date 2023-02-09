def solution(babbling):
    x = ["aya", "ye", "woo", "ma"]
    a,b,c,d = [],[],[],[]
    
    for i in x:
        a.append(i)
    for i in x:
        for j in x:
            if i!=j:
                b.append(i+j)
    for i in x:
        for j in x:
            for k in x:
                if i != j and i != k and j != k:
                    c.append(i+j+k)
    for i in x:
        for j in x:
            for k in x:
                for v in x:
                    if i != j and i != k and i !=v and j != k and j != v and k != v:
                        d.append(i+j+k+v)
    bab= a+b+c+d

    count = 0
    for i in babbling:
        if i in bab:
            count +=1

    return count
'''
solution:
고등학교떄 배운 P (permutation)이 생각나서 해당 변수를 모두 한 리스트에 저장 후
babbling 과 비교하는 식으로 직행했습니다.

시간복잡도 시각에서 for문을 4번이나 썻기 떄문에 매우 효율적이지 못한 코드입니다...
'''