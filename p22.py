size = 10
table = [[] for _ in range(size)]

def insert(key):
    index = key % size
    table[index].append(key)

insert(23)
insert(43)
insert(13)
insert(25)

for i in range(size):
    print(i, "->", table[i])