s = input()

ee_cnt = 0
eb_cnt = 0

for i in range(len(s)-1):
    if s[i:i+2] == 'ee':
        ee_cnt += 1
    if s[i:i+2] == 'eb':
        eb_cnt += 1

print(ee_cnt, eb_cnt)