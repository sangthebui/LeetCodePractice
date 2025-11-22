# Dynamic Programming

- DP is primarily a method for solving complex problems by breaking them down into simpler subproblems.

- The core idea of DP relies on two properties: **optimal substructure** (the optimal solution to the overall problem can be constructed from the optimal solutions to its subproblems) and **overlapping subproblems** (the same subproblems are solved repeatedly).

- DP avoids redundant calculations by storing the results of subproblems, a technique known as memoization (top-down DP) or tabulation (bottom-up DP).

- Memoization is a top-down approach where the problem is solved recursively, and a lookup table (e.g., an array or hash map) is used to cache results of subproblems as they are computed.

- Tabulation is a bottom-up approach where you solve the subproblems first (usually starting with the base cases) and store their results in a table, then use these results to compute the solutions to larger subproblems until the main problem is solved.

- Commonly used data structures in DP are arrays or tables (often multi-dimensional) to store the intermediate results and track the optimal solutions for subproblems.

- Classic examples of problems solved efficiently using dynamic programming include the Fibonacci sequence, the Knapsack Problem, the Longest Common Subsequence (LCS), and the minimum path sum in a grid.

```python
def fib_tab(n):
    """
    Calculates the n-th Fibonacci number using Tabulation (Bottom-Up DP).
    F(n) = F(n-1) + F(n-2)
    """
    if n <= 1:
        return n

    # 1. Initialize DP Table
    # The table size is (n + 1) to store results from index 0 up to n.
    dp_table = [0] * (n + 1)

    # 2. Define Base Cases in the table
    dp_table[0] = 0
    dp_table[1] = 1

    # 3. Fill the DP Table Iteratively
    # The iterative structure is the core of bottom-up DP.
    for i in range(2, n + 1):
        # State Transition/Recurrence Relation
        # The solution for 'i' depends directly on previously computed solutions.
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

    # 4. Return the Final Solution
    return dp_table[n]

```

```python
memo = {}

def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

# top down
def min_coin(target, coins):
    if target in memo:
        return memo[target]

    if target == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = target - coin
            if subproblem < 0:
                continue
            answer = min_ignore_none(answer, min_coin(subproblem, coins) + 1)
    memo[target] = answer
    return answer

# bottom up
def min_coin(target, coins):
    memo = {}
    memo[0] = 0
    for i in range(1, target + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i)], memo[subproblem] + 1)
    return memo[target]

# how many ways instead of the minimum
from collections import defaultdict
def how_many_ways(target, coins):
    memo = defaultdict(lambda _ : 0)
    memo[0] = 1
    for i in range(1, target + 1):
        memo[i] = 0

        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] += memo[subproblem]
    return memo[target]

print(how_many_ways(5, [1, 4, 5])) # 4
print(how_many_ways(87, [1, 4, 5])) # 828851371566224

```
