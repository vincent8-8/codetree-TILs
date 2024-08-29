n, m, k = map(int, input().split())

students = [0] * 100
for _ in range(m):
    student = int(input())
    students[student] += 1
    if students[student] >= k:
        print(student)
        break
if max(students) < k:
    print("-1")