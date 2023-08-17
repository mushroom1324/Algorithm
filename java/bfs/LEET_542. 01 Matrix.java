class Pair {
    public int x;
    public int y;
    public int d;

    Pair(int x, int y, int d) {
        this.x = x;
        this.y = y;
        this.d = d;
    }
}

class Solution {
    
    private Queue<Pair> queue = new LinkedList<>();
    private int m;
    private int n;
    private int[][] mat;

    public int[][] updateMatrix(int[][] mat) {
        this.mat = mat;

        m = mat.length;
        n = mat[0].length;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 0) queue.add(new Pair(i, j, 0));
                else mat[i][j] = Integer.MAX_VALUE;
            }
        }

        bfs();
        
        return mat;
        
    }

    private void bfs() {

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        while (!queue.isEmpty()) {
            Pair cur = queue.poll();

            if (mat[cur.x][cur.y] >= cur.d) mat[cur.x][cur.y] = cur.d;
            else continue;

            for(int k = 0; k < 4; k++) {
                int nx = dx[k] + cur.x;
                int ny = dy[k] + cur.y;

                if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                    queue.add(new Pair(nx, ny, cur.d + 1));
                }
            }
            
        }

    }
}
