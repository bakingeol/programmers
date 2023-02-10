def solution():
    a_1 = [1, 2, 3, 3, 3, 3, 3, 4]
    a_2 = [1, 1, 2, 2]
    a_3 = [1]
    count = 0
    dict_1 = {}
    for index, value in enumerate(a_1):
        count = a_1.count(value)
        if value not in dict_1:
            dict_1[value] = count
            
    result = [k for k,v in dict_1.items() if max(dict_1.values())==v]
    # max(dict_1,key=dict_1.get)
    if len(result) > 1:
        return -1
    else:
        return result[0]

'''
solution : dictionary형태로 key에 숫자, value에 카운트 숫자를 넣어준 후 리스트 컴프리헨션을 이용해(중복값 잡기 위해) 
return. result 자리에 아래 # 형식을 넣어도 동일하게 dictionary에서 max값 출력이 가능
key = dict_1.get 을 사용하면 각 키에 대한 값을 기준으로 키를 비교함
'''

        

