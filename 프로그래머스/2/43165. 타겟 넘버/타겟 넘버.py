answer=0

def dfs(numbers,target, current, idx):
    global answer
    
    if len(numbers)==idx:
        if target==current:
            answer+=1
        return
    else:
        dfs(numbers,target,current+numbers[idx],idx+1)
        dfs(numbers,target,current-numbers[idx],idx+1)

def solution(numbers, target):
    dfs(numbers,target,0,0)
    return answer