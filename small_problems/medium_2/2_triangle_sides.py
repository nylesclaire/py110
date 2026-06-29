
def is_invalid_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    longer_side = max(sides)
    shorter_two_sides = sides.copy()
    shorter_two_sides.remove(longer_side)

    if sum(shorter_two_sides) <= longer_side or (0 in sides):
        return True

def triangle(side1, side2, side3):
    if is_invalid_triangle(side1, side2, side3):
        return "invalid"
    
    if side1 == side2 == side3:
        return "equilateral"
    elif (
        (side1 == side2 and side1 != side3)
        or (side1 == side3 and side1 != side2)
        or (side2 == side3 and side2 != side1)
    ):
        return "isoceles"
    else:
        return "scalene"


# Examples
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isoceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
