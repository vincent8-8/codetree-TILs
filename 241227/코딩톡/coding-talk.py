n, m, p = map(int, input().split())
_messages = [list(input().split()) for _ in range(m)]
_people = []

for i in range(n):
    _people.append(chr(i + 65))

for i in range(p - 1, m):
    person = _messages[i][0]
    if person in _people:
        _people.remove(person)

for i in range(p - 1, -1, -1):
    if _messages[i][1] ==_messages[p - 1][1]:
        if _messages[i][0] in _people:
            _people.remove(_messages[i][0])

if _messages[p - 1][1] == '0':
    print("")
else:
    for person in _people:
        print(person, end=" ")