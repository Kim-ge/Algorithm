def solution(price, money, count):
    answer = -1
    total=0
    for i in range(1,count+1):
        tmp=price*i
        total+=tmp
    if total>money:
        answer=total-money
    if total<=money:
        answer=0
    return answer