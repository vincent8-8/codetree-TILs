n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]
cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            is_answer = True
            graph = [ 0 for _ in range(101)]

            for l in range(n):
                if l in (i, j, k):
                    continue
                
                s, e =  _list[l]
                for q in range(s, e + 1):
                    graph[q] += 1
            
            for w in range(101):
                if graph[w] > 1:
                    is_answer = False
                    break
            
            if is_answer:
                cnt += 1
print(cnt)