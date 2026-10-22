n = int(input())

solved = 0
for i in range(0, n):
    problem = list(map(int, input().split()))
    count = 0

    for element in problem:
        if element == 1:
            count += 1

    if count >= 2:
        solved += 1

print(solved)
