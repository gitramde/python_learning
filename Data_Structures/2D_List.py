"""
Multi-Dimensional List/ 2D Grids:
    A nested list is a list that contains other lists.

    This is a 2D list, where each element is a list of integers.

    nested_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
"""
# Initialization of 2D list

grid = [[0 for i in range(3)] for j in range(2)]

grid[0][0] = 1

print(grid) # [[1, 0, 0], [0, 0, 0]]

grid = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(grid)    # 2
cols = len(grid[0]) # 3

print(f"Number of Rows: {rows}")
print(f"Number of cols: {cols}")

print (f"Number at 2nd row, 2nd column [1][1]: {grid[1][1]}")
