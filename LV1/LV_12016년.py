import datetime
def solution(a,b):
    x = datetime.date(2016,a,b)
    return x.strftime('%a').upper()