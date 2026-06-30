def is_invalid_triangle(angles_list):
    if sum(angles_list) != 180 or min(angles_list) <= 0:
        return True
    
def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]

    if is_invalid_triangle(angles):
        return "invalid"
    
    if 90 in angles:
        return "right"
    elif max(angles) > 90:
        return "obtuse"
    return "acute"

# Test cases
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True