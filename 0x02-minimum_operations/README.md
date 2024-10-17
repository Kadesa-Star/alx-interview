Key Concepts
Prime Factorization:
The problem boils down to finding the sum of the prime factors of a number. For any number n, the minimum operations are essentially the sum of its prime factors. Why? Because each prime factor tells you how many "Paste" operations you'll need after copying a portion of the text. For example, for n = 9, its prime factorization is 3 * 3, which means that you need two sets of operations (copy, paste, paste) to get to 9.

Greedy Approach:
You can implement a greedy algorithm that continuously divides the target number n by its smallest prime factor, keeping track of the operations involved until you reduce n to 1. This is efficient in determining the optimal sequence of operations.

Dynamic Programming:
You can also solve this problem using dynamic programming (DP) to store intermediate results and reduce repeated calculations, although for this particular problem, a greedy approach is often sufficient.

Steps to Solve
Prime Factorization Approach:

Start with a given number n.
Find the smallest prime factor p of n.
Reduce n by dividing it by p and repeat the process.
Each division corresponds to a "Copy All" followed by several "Paste" operations.
The sum of the factors gives the minimum number of operations.
Mathematical Insight:

If n is a prime number, the minimum number of operations is n itself (1 "Copy All" and n-1 "Paste").
If n is a composite number, break it down into smaller factors.
