import math

def degree_to_radian(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Example degree value
degrees_value = 90

radians_value = degree_to_radian(degrees_value)

print(degrees_value, "degrees is equal to", radians_value, "radians.")
