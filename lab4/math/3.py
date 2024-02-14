import math

def regular_polygon_area(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

# Example values
num_sides = 6  # Number of sides
side_length = 5  # Length of each side

area = regular_polygon_area(num_sides, side_length)

print("The area of the regular polygon is:", area)
