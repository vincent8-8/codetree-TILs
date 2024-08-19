n = int(input())
_listA = list(map(int, input().split()))
_listB = list(map(int, input().split()))

def f(n):
    for i in range(n):
        if _listA[i] != _listB[i]:
            return False
    return True

_listA = sorted(_listA)
_listB = sorted(_listB)

if f(n):
    print("Yes")
else:
    print("No")