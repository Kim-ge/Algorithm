from collections import deque
queue = deque()

num=int(input())

for i in range(1,num+1):
    queue.append(i)

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])