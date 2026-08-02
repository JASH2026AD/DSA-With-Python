size = 10
table = [None] * size

def insert(key):
    original_index = key % size
    i = 0

    while i < size:
        index = (original_index + i * i) % size

        if table[index] is None:
            table[index] = key
            return

        i += 1

    print("Hash table is full")

insert(23)
insert(43)
insert(13)
insert(25)

for i in range(size):
    print(i, "->", table[i])