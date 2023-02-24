def solution(s):
    dictionary = {'zero': 0, 'one' :1,'two':2, 'three' : 3, 'four' : 4, 'five': 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 
                  '0':0,'1' :1, '2': 2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

    x = ''
    result = ''
    for i in s:
        x += i
        if x in set(dictionary.keys()):
            result += str(dictionary[x])
            x = ''
    return int(result)
          
'''
solution : 
dictionary 형성 후 하나씩 바꿔주기..
'''
# 다른사람 풀이 
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)