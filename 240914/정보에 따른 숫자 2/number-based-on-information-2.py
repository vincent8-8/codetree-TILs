t, a, b  = map(int, input().split())
_list = [
    list(input().split())
    for _ in range(t)
]

graph = [ 0 for _ in range(1001)]

for alph, idx in _list:
    idx = int(idx)
    graph[idx] = alph

# S 가 N 보다 가까이 혹은 같으면 특별한 위치
answer_cnt = 0

def find_pos(idx, alph):
    if idx == 1000:
        return 1
    elif graph[idx] == alph:
        return 1
    
    return find_pos(idx + 1, alph) + 1


def find_neg(idx, alph):
    if idx == 0:
        return 1
    elif graph[idx] == alph:
        return 1
    
    return find_neg(idx - 1, alph) + 1

for i in range(a, b + 1):
    if graph[i] == "N":
        continue
    elif graph[i] == "S":
        answer_cnt += 1
        continue
    
    d_to_N = min(find_pos(i, "N"), find_neg(i, "N"))
    d_to_S = min(find_pos(i, "S"), find_neg(i, "S"))

    if d_to_N >= d_to_S:
        answer_cnt += 1

    
    

print(answer_cnt)