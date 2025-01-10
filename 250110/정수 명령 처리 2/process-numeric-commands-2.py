N = int(input())
commands = [list(input().split()) for _ in range(N)]

# Write your code here!
from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        if self.empty():
            return "The Queue is empty"
        
        return self.dq.popleft()
    
    def front(self):
        if self.empty():
            return "The Queue is empty"
        
        return self.dq[0]

dq = Queue()


for command in commands:
    if len(command) == 1:
        order = command[0]

        if order == "front":
            print(dq.front())
        elif order == "pop":
            print(dq.pop())
        elif order == "size":
            print(dq.size())
        else:
            if dq.empty() == 0:
                print(0)
            else:
                print(1)
    else:
        dq.push(int(command[1]))
