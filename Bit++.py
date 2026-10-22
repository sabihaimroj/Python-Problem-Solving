n = int(input())
x = 0

for i in range(0, n):
    opt = input()
    if "+" in opt:
        x += 1
    elif "-" in opt:
        x -= 1

print(x)
