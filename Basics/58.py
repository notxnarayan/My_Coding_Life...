def name_gen(n):
    for name in n:
        yield name

# Object creation
s = ['Alice', 'Bob', 'Charlie']
ret = name_gen(s)

for name in ret:
    print(f"Student: {name}")
