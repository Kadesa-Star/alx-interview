#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    k = []
    if n <= 0:
        return k  # Return empty list for non-positive n
    k = [[1]]  # Start with the first row

    for i in range(1, n):  # Loop to generate each row
        temp = [1]  # Start each row with a 1
        for j in range(len(k[i - 1]) - 1):  # Iterate over the previous row
            curr = k[i - 1]  # Reference the previous row
            # Calculate the sum of the two elements above
            temp.append(curr[j] + curr[j + 1])
        temp.append(1)  # End each row with a 1
        k.append(temp)  # Append the new row to the triangle
    return k  # Return the complete triangle
