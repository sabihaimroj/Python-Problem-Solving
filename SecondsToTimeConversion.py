s = int(input())

H = int(s / 3600)
M = int((s % 3600) / 60)
S = int((s % 3600) % 60)

print(f"{H}:{M}:{S}")

