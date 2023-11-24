from collections import deque

queue = deque([])
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')


print(queue)
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()

if not queue:
    print('empty')
print(queue)