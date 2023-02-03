n = 10
i = 1
while i <= n:
    a = list(str(i))
    if '3' in a or i % 3 ==0:
        n += 1 
    i += 1
print(n)

''' solution
3x 마을에서 쓰는 숫자는 n 으로 생각하고 i를 1~n까지 3의배수 or 3숫자가 들어가 있는 것을 
검증해보면서 n을 업데이트(i가 조건식에 걸리면 n값을 증가시켜 while문이 더 돌아갈 수 있게 함)
'''