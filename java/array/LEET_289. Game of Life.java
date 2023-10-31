class Solution {

    private int[][] ways = {{1, 0}, {-1, 0}, {0, 1}, {-1, 1}, {1, 1}, {0, -1}, {1, -1}, {-1, -1}};

    private int n, m;

    public void gameOfLife(int[][] board) {
        n = board.length;
        m = board[0].length;

        int[][] next = new int[n][m];

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                check(i, j, board, next);
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                board[i][j] = next[i][j];
            }
        }
        
    }

    private void check(int i, int j, int[][] board, int[][] next) {
        int cnt = 0;

        for (int[] way : ways) {
            int dx = i + way[0];
            int dy = j + way[1];

            if (0 <= dx && 0 <= dy && dx < n && dy < m && board[dx][dy] == 1) {
                ++cnt;
            }
                
        }

        if (board[i][j] == 0) {
            if (cnt == 3) next[i][j] = 1;
        }
        else {
            if (cnt == 3 || cnt == 2) next[i][j] = 1;
        }
    }
}
