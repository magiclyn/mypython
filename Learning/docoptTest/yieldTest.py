def parse():
    for a in range(5):
        yield a

b = parse()
print(b)

for a in b:
    print(a)    