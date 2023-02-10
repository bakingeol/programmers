from fractions import Fraction
def solution(dots):
    
    a = Fraction(dots[0][0] - dots[1][0], dots[0][1] - dots[1][1])
    b = Fraction(dots[2][0] - dots[3][0], dots[2][1] - dots[3][1])
    if a==b:
        return 1
    a = Fraction(dots[0][0] - dots[2][0], dots[0][1] - dots[2][1])
    b = Fraction(dots[1][0] - dots[3][0], dots[1][1] - dots[3][1])
    if a==b:
        return 1
    a = Fraction(dots[0][0] - dots[3][0], dots[0][1] - dots[3][1])
    b = Fraction(dots[1][0] - dots[2][0], dots[1][1] - dots[2][1])
    if a==b:
        return 1
    else:
        return 0
'''
solution:
Fraction -> 기약분수로 나타내는 함수를 이용해 기울기가 같으면 평행으로 생각
단순노동코드...
'''