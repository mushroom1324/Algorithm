class Solution {
    int[][] dp;
    int m;
    int n;

    public int uniquePaths(int m, int n) {

        this.m = m;
        this.n = n;

        // using dp
        dp = new int[m][n];
        for (int[] each : dp) {
            Arrays.fill(each, -1);
        }

        dp[0][0] = 1;

        // find and save the number of unique paths in dp
        // find them in increasing order.
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) continue;
                dp[i][j] = finder(i - 1, j) + finder(i, j - 1);
            }
        }
        return dp[m-1][n-1];
    }

    private int finder(int x, int y) {
        // finder(m, m) := finder(m - 1, n) + finder(m, n - 1)
        // finder(0, 0) = 1
        if (x < 0 || x > m - 1 || y < 0 || y > n - 1) return 0;
        return dp[x][y];
    }
}
