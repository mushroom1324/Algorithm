class Pair {
    int x, y;

    Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public int[][] dp;
    public int maxVal;

    public int n, m;
    
    public int maxAreaOfIsland(int[][] grid) {
        m = grid.length;
        n = grid[0].length;

        dp = new int[m][n];

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1 && dp[i][j] == 0) {
                    bfs(i, j, grid);
                }
            }
        }
            
        return maxVal;
    }

    private void bfs(int i, int j, int[][] grid) {
        Deque<Pair> q = new ArrayDeque<>();

        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};

        int cnt = 1;
        dp[i][j] = 1;

        q.add(new Pair(i, j));

        while (!q.isEmpty()) {
            Pair cur = q.removeFirst();

            for(int k = 0; k < 4; ++k) {
                int nx = dx[k] + cur.x;
                int ny = dy[k] + cur.y;
                
                if (nx >= 0 && ny >= 0 && nx < m && ny < n 
                && dp[nx][ny]++ == 0 && grid[nx][ny] == 1) {
                    q.add(new Pair(nx, ny));
                    cnt++;
                }
            }
        }

        maxVal = Math.max(maxVal, cnt);
    }
}
