def solution(left, right):
    answer = 0
    
    for number in range(left, right + 1):
        count = 0
        
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1 #약수의 개수 구하기
        
        if count % 2 == 0: #약수의 개수가 짝수인 경우
            answer += number
        else:
            answer -= number #약수의 개수가 홀수인 경우
    
    return answer
