def trapezoid_area(a, b, h):
    area = 0.5 * (a + b) * h
    return area

# Example values
side_a = 5
side_b = 7
height = 4

area = trapezoid_area(side_a, side_b, height)

print("The area of the trapezoid is:", area)
