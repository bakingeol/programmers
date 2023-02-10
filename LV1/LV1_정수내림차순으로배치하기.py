def solution(n):
    return int(''.join(sorted(list(str(n)),reverse = True)))

'''
solution:
정수 -> 문자 -> list -> sorted reverse(list return), -> str -> int
'''