n = int(input())

for i in range(0, n):
    word = input()
    length = len(word)

    if length <= 10:
        print(word)
        continue

    print((word[0]+str(length-2)+word[length-1]))
