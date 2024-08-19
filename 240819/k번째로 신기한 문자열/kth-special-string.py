n, k, t = input().split()

_list = [
    input() for _ in range(int(n))
]

len_t = len(t)
target = []

for elem in _list:
    if elem[0:len_t] == t:
        target.append(elem)
    
target.sort()
print(target[int(k) - 1])