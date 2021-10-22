def fileSwap(a, b):
    with open(a, 'r') as f:
        f1 = f.read()
    with open(b, 'r') as f:
        f2 = f.read()
    with open(a, 'w') as f:
        f.write(f2)
    with open(b, 'w') as f:
        f.write(f1)

fileSwap(input("What is the first files name?\n"), input("What is the second files name?\n"))
print("Swapping Complete!")