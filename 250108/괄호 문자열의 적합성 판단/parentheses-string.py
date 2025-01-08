command = input()

# Write your code here!
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def empty(self):
        if self.items:
            return False
        else:
            return True
    
    def pop(self):
        if self.empty() == True:
            return "This stack is empty"
        
        return self.items.pop()

s = Stack()
answer = True

for c in command:
    if c == "(":
        s.push("(")
    else:
        if s.empty() == True:
            answer = False
            break
        else:
            s.pop()

if s.empty() == False or answer == False:
    print("No")
else:
    print("Yes")
