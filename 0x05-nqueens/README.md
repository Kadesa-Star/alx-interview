* Solution Outline with Backtracking and Recursion
==================================================

To solve the problem, implement a recursive backtracking 
algorithm. Here’s a breakdown of how to approach the solution:

Board Representation:
-----------------------
Represent the board as a list of integers where the index 
is the row, and the value at each index is the column 
position of the queen in that row.

Backtracking Function:
----------------------
Define a recursive function that attempts to place queens 
row by row.
Use helper functions to check for conflicts before placing 
a queen in a specific row and column.

Validation Function:
----------------------
The is_safe function ensures no two queens share the 
same column or diagonal.

Main Recursive Function:
-------------------------
Place a queen in each row, recursively trying each column, 
and backtrack if no valid column is found in the current row.
