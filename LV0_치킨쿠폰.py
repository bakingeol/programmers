def solution(chicken):
    answer = []
    coupon = []
    result = chicken
    while result > 0:
        result = chicken//10
        answer.append(result)
        coupon.append(chicken%10)
        chicken = result
    answer.append((sum(coupon)//10 + sum(coupon)%10)//10)
    answer.append(sum(coupon)//10)
    return sum(answer)

'''
solution:
쿠폰 10게에 치킨 1개, 쿠폰 1개가 생기므로 몫과 나머지를 이용 
line10 에서는 나머지 부분의 합산이 예를들어 28이 나왔을 때
1개가 더 answer에 추가 되야 하는 점을 넣음
'''