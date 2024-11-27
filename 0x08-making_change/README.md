
This project sounds exciting and challenging! Let’s break it down so you can tackle the coin change problem effectively. Here's a structured approach tailored to your project's requirements:

Understanding the Problem
The goal is to:

Minimize the number of coins required to make up a given amount.
Use a list of coin denominations provided.
Key Challenges:

Choosing the right algorithm (Greedy or Dynamic Programming) based on the constraints.
Ensuring efficiency in both time and space complexity.
Approaches
1. Greedy Algorithm
How it works: Always pick the largest coin denomination that fits into the remaining amount.
When it works: If the coin denominations are canonical (like US coins: 1, 5, 10, 25).
Limitation: Might fail for certain denominations where the optimal solution requires combining smaller coins.
2. Dynamic Programming
How it works: Solve subproblems for smaller amounts and build up to the total amount.
Optimal Substructure: If the solution for amount x is optimal, the solution for amount x - coin must also be optimal.
Overlapping Subproblems: Reuse results for the same amount multiple times.
Implementation Plan
Task: Write a function makeChange(coins, total):
Input:
coins: List of coin denominations (e.g., [1, 2, 5]).
total: The target amount.
Output: Minimum number of coins required to make up the total, or -1 if it’s not possible.
