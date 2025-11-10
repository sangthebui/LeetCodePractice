# farmer
- A farmer wants to farm their land with the maximum area where good land is present. The "land" is represented as a matrix with 1s and 0s, where 1s mean good land and 0s mean bad land. The farmer only want to farm in a square of good land with the maximum area. Please help the farm to find the maximum area of the land they can farm in good land.

- Example:
0 1 1 0 1
1 1 0 1 0
0 1 1 1 0
1 1 1 1 0
1 1 1 1 1
0 0 0 0 0

## answer
def max_farmland_area(land):
    m, n = len(land), len(land[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if land[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return max(max(row) for row in dp)