t , w = map(int, input().split())

result = t // w

if t % w > 0 :
    result = result + 1

print(result)

