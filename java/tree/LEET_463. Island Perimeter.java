class Pair {
    public int x;
    public int y;

    Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {

    private int ans = 0;
    private int row;
    private int col;

    public int islandPerimeter(int[][] grid) {

        row = grid.length;

        if (row == 0) return 0;

        col = grid[0].length;

        for(int i = 0; i < row; ++i) {
            for(int j = 0; j < col; ++j) {
                if (grid[i][j] == 1) {
                    helper(i, j, grid);
                    return ans;
                }
            }
        }
        return ans;

    }

    public void helper(int i, int j, int[][] grid) {
        Queue<Pair> queue = new LinkedList<>();

        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};

        grid[i][j] = 2;
        queue.add(new Pair(i, j));

        while(!queue.isEmpty()) {
            Pair cur = queue.poll();

            for(int k = 0; k < 4; k++) {
                int nx = cur.x + dx[k];
                int ny = cur.y + dy[k];

                if (0 <= nx && nx < row && 0 <= ny && ny < col) {
                    if (grid[nx][ny] == 1) {
                        grid[nx][ny] = 2;
                        queue.add(new Pair(nx, ny));
                        continue;
                    }
                    if (grid[nx][ny] == 0) {
                        ++ans;
                        continue;
                    }

                } else {
                    ++ans;
                }

            }
        }

    }
}