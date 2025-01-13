from collections import deque

n = int(input())
commands = [list(input().split()) for _ in range(n)]

# Write your code here!
dq = deque()

for command in commands:
    if len(command) == 2:
        if command[0] == "push_back":
            dq.append(int(command[1]))
        else:
            dq.appendleft(int(command[1]))
    else:
        if command[0] == "pop_front":
            print(dq.popleft())
        elif  command[0] == "pop_back":
            print(dq.pop())
        elif  command[0] == "size":
            print(len(dq))
        elif  command[0] == "empty":
            if dq:
                print(0)
            else:
                print(1)
        elif command[0] == "front":
            print(dq[0])
        else:
            print(dq[-1])
