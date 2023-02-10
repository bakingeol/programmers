from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    a = Fraction(numer1, denom1)
    b = Fraction(numer2, denom2)
    result = a + b
    
    return [result.numerator, result.denominator]
'''
solution : Fraction 외장함수를 사용하면 기약분수를 빠르게 구할 수 있다.
분자는 numerator, 분모는 denominator으로 int형 리턴해준다.
'''