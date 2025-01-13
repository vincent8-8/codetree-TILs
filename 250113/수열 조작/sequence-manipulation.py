n = int(input())

# Write your code here!
from collections import deque

dq = deque()
last = 0

for i in range(1, n + 1):
    dq.append(i)

while dq:
    last = dq.popleft()
    if dq:
        dq.append(dq.popleft())

print(last)