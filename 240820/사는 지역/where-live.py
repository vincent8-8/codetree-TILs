n = int(input())
_list = [
    tuple(input().split())
    for _ in range(n)
]

class C:
    def __init__(self, name="", num="", location=""):
        self.name = name
        self.num = num
        self.location = location
    
cs = [C() for _ in range(n)]
index = 0

for i in range(n):
    name, num, location = _list[i]

    cs[i].name = name
    cs[i].num = num
    cs[i].location = location

    if cs[i].name > cs[index].name:
        index = i
        
print(f"name {cs[index].name}")
print(f"addr {cs[index].num}")
print(f"city {cs[index].location}")