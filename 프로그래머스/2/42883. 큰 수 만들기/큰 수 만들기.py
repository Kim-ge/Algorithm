def solution(number, k):
    stack = []
    for num in number:
        #현재 숫자가 스택의 마지막 숫자보다 크면 스택에서 숫자를 제거하고, 제거 횟수 줄이기
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    #제거할 요소가 있으면 끝에서 제거
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)