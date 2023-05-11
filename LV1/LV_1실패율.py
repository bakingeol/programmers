from collections import Counter
def solution(N, stages):
    dic = Counter(stages)

    for i in range(1, N+2):
        if i not in dic:
            dic[i] = 0
    dic = dict(sorted(dic.items(), key=lambda x:x[0]))

    x=len(stages)
    for i in dic:
        if x==0:
            dic[i] = 0
            break
        a = dic[i]
        dic[i] = dic[i]/x
        x = x-a

    del dic[N+1]

    return list(dict(sorted(dic.items(), reverse=True,key = lambda x:x[1])).keys())