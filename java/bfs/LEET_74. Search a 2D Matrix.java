class Coord {
    public int n;
    public int m;

    Coord(int n, int m){
        this.n = n;
        this.m = m;
    }
}

class Solution {

    public boolean searchMatrix(int[][] matrix, int target) {
        Queue<Coord> queue = new LinkedList<>();
        int max_n = matrix.length;
        if (max_n == 0) return false;
        int max_m = matrix[0].length;

        int cur_max = -1000000;

        queue.add(new Coord(0, 0));

        while (queue.peek() != null) {
            Coord cur = queue.poll();
            int val = matrix[cur.n][cur.m];

            if (val == target) return true;
            else if (val > target) continue;

            cur_max = Math.max(cur_max, val);
            if (val < cur_max) continue;

            if (cur.n + 1 < max_n) queue.add(new Coord(cur.n + 1, cur.m));
            if (cur.m + 1 < max_m) queue.add(new Coord(cur.n, cur.m + 1));

        }
        return false;
    }
}