size = 10
table = [None] * size

def insert(key):
    index = key % size

    while table[index] is not None:
        index = (index + 1) % size

    table[index] = key

insert(23)
insert(43)
insert(13)
insert(25)

for i in range(size):
    print(i, "->", table[i])