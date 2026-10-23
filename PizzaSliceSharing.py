pizzaSlices , friends = map(int, input().split())

wholeSlices = int(pizzaSlices / friends)
remainingSlices = int(pizzaSlices % friends)

print(wholeSlices, remainingSlices)


