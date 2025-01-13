n, k = map(int, input().split())

# Write your code here!
from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def size(self):
        return len(self.dq)
    
    def empty(self):
        return self.dq
    
    def top(self):
        return self.dq[0]
    
    def pop(self):
        return self.dq.popleft()

dq = Queue()
dq2 = Queue()

for i in range(1, n + 1):
    dq.push(i)

for _ in range(n):
    if dq.size() == 1:
        print(dq.top())
        break

    for _ in range(k - 1):
        if dq.empty():
            while not dq2:
                dq.push(dq2.pop())
            dq.push(dq.pop())
        else:
            dq2.push(dq.pop())
    while dq2.empty():
        dq.push(dq2.pop())

    print(dq.pop(), end=" ")