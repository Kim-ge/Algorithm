def solution(s):
    answer = True
    s1=s.lower()
    
    char1=s1.count('p')
    char2=s1.count('y')
    
    if char1==char2:
        return True
    elif char1!=char2:
        return False
    elif char1==0 and char2==0:
        return True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True