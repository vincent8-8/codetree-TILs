n = int(input())
s = input()

min_len = n

for i in range(1, n):
    local_len = 101
    # 문자열 설정
    target = s[0:i]
    if target in s[i:]:
        continue
    
    min_len = i
    break

print(min_len)