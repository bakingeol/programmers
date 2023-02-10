def solution(phone_number):
    return '*'*len(phone_number[:-4])+phone_number[-4:]

'''
solution:
배열 슬라이싱을 이용해 뒤에서 4번째 이후는 *로 표시하고 뒤에서 4개 숫자를 더해준다.
'''