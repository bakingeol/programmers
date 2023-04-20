def solution(k, score):
    result = []
    k_list = []
    
    for i in score:
        k_list.append(i)
        k_list = sorted(k_list)
        if len(k_list)> k:
            del k_list[0]
        result.append(k_list[0])
    return result