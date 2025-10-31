def solution(array, commands):
    answer =[]
    
    for i in range(0,len(commands)):
        a=commands[i][0]
        b=commands[i][1]
        c=commands[i][2]
        
        newarr=sorted(array[a-1:b])
        answer.append(newarr[c-1])
        
    return answer