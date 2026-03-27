def calculate_leftover_blocks(provided_blocks):
    available_blocks = provided_blocks
    layer = 0
    blocks_in_this_layer = 0
    while blocks_in_this_layer <= available_blocks:
        available_blocks -= blocks_in_this_layer
        layer += 1
        blocks_in_this_layer = layer * layer
    return available_blocks


# test cases
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True