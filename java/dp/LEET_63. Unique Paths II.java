class Solution {

    private int[][] dp;
    private int[][] grid;

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        this.grid = obstacleGrid;

        int n = grid.length;
        int m = grid[0].length;

        dp = new int[n][m];
        for (int[] each: dp) Arrays.fill(each, -1);
        dp[0][0] = 1;

        return find(n - 1, m - 1);
    }

    private int find(int x, int y) {

        if (x < 0 || y < 0) return 0;
        if (grid[x][y] == 1) return 0;
        if (dp[x][y] != -1) return dp[x][y];

        dp[x][y] = find(x - 1, y) + find(x, y - 1);
        return dp[x][y];
    }
}
