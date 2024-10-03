#!/usr/bin/python3


def pascal_triangle(n):
    """Generate Pascal's Triangle of height n."""
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        # Initialize a new row with 1's at the edges
        row = [1] * (i + 1)
        
        # Each element (except for the edges) is the sum of the two elements above it
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Append the new row to the triangle
        triangle.append(row)
    
    return triangle
