class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        sol = [0 for _ in range(n + 1)]
        sol[0] = 1
        for i in range(1, 1 + n):
            for j in range(i):
                sol[i] += sol[j] * sol[i - j - 1]
        return sol[n]