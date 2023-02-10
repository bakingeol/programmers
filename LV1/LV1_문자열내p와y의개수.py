def solution(a):
    a = a.lower()
    if a.count('p') == a.count('y'):
        return True
    else:
        return False
    
'''
solution:
들어오는 문자를 소문자로 만든 후 p와 y의 개수를 count
'''