def solution(s,n):  # 대문자 65~90 소문자 97~122
    result = ''
    for i in s:
        if 65<= ord(i) <=90:
            if 90 < ord(i) + n:
                result += chr(ord(i) + n -26)
            else:
                result += chr(ord(i) + n)
        elif 97<= ord(i) <=122:
            if 122 < ord(i) + n:
                result += chr(ord(i) + n -26)
            else:
                result += chr(ord(i) + n)
        else:
            result += ' '
    return result
'''
solution:
아스키코드를 활용한다.
chr(숫자) -> 숫자에 맞는 아스키코드로 변환 (리턴값 문자)
ord('문자') -> 아스키 코드로 변환(리턴값 숫자)
'''