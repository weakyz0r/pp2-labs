def parallelogram_area(base, height):
    area = base * height
    return area

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = parallelogram_area(base, height)

print("Expected Output:", area)
