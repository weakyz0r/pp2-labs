def squares(a, b):
    for num in range(a, b+1):
        yield num ** 2

a = 3  # Start number
b = 7  # End number

print("Squares of numbers from", a, "to", b, "are:")
for square in squares(a, b):
    print(square)
