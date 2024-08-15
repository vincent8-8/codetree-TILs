n, m = map(int, input().split())
_list = list(map(int, input().split()))

def calculate(a, b):
    result = 0
    for i in range(a-1, b):
        result += _list[i]
    print(result)

for _ in range(m):
    a, b = map(int, input().split())
    calculate(a, b)