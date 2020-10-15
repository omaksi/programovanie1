filename = input()

with open(f'./{filename}', 'r') as f:
    f.readline()
    print(f.readline())
