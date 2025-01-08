N = int(input())
commands = [list(input().split()) for _ in range(N)]

# Write your code here!
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        if not self.items:
            return 1
        else:
            return 0
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]

s = Stack()

for command in commands:
    if len(command) == 2:
        s.push(command[1])
    else:
        if command[0] == "size":
            print(s.size())
        elif command[0] == "pop":
            print(s.pop())
        elif command[0] == "empty":
            print(s.empty())
        else:
            print(s.top())
        
