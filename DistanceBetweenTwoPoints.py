import math
X1,Y1, x1,y1 = map(int, input().split())

d = math.sqrt((X1-x1)**2 + (Y1-y1)**2)

print(f"{d:.4f}")


