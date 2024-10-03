To implement Pascal's Triangle in Python, we will define a function called pascal_triangle(n). This function will generate a list of lists representing Pascal's Triangle for a given number of rows, n. Here’s how to approach this:

Function Definition: The function should take one parameter, n, which represents the number of rows in the triangle.
Return Empty List for Invalid Input: If n is less than or equal to 0, the function should return an empty list.
Generate the Triangle:
Start with the first row, which is always [1].
For each subsequent row, calculate the values based on the previous row.
Each element in the current row (except for the edges) is the sum of the two elements directly above it in the previous row.
The edges of the triangle will always be 1.
