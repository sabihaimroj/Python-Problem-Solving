d = int(input())

Y = int(d / 365)
M = int((d % 365) / 30)
D = int((d % 365) % 30)

print(f"{Y} years")
print(f"{M} months")
print(f"{D} days")