def trapezoid_area(height, base1, base2):
    area = (base1 + base2) * height / 2
    return area

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

result = trapezoid_area(height, base1, base2)
print("Expected Output:", result)
