class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        
        Arrays.fill(dp, Integer.MAX_VALUE);

        dp[0] = 0;
        int ind = 1;

        while (ind * ind <= n) {
            int square = ind * ind;

            for (int i = square; i <= n; ++i)
                dp[i] = Math.min(dp[i - square] + 1, dp[i]);
            ++ind;
            
        }

        return dp[n];
    }
}

/*
==== PREVIOUS SOLUTION : Time 8.11%, Memory 5.14% ====

class Pair {
    int sum, cnt;

    Pair(int sum, int cnt) {
        this.sum = sum;
        this.cnt = cnt;
    }
}

class Solution {
    public int numSquares(int n) {
        
        // get every possible nums that are smaller than n

        // bfs through every nodes.

        // Queue<Pair>, Pair = sum + cnt

        // if dp[sum] != 0 && dp[sum] < cur, continue

        // return least cnt that are reached to n.

        List<Integer> ways = new ArrayList<>();
        for (int i = 1; i * i <= n; ++i) {
            ways.add(i * i);
        }

        Deque<Pair> q = new ArrayDeque<>();
        q.add(new Pair(0, 0));

        int[] dp = new int[n + 1];

        while (!q.isEmpty()) {
            Pair cur = q.removeFirst();

            if (dp[cur.sum] != 0 && dp[cur.sum] <= cur.cnt) continue;
            dp[cur.sum] = cur.cnt;

            for (Integer each : ways) {
                if (cur.sum + each > n) break;
                q.add(new Pair(cur.sum + each, cur.cnt + 1));
            }
            
        }

        return dp[n];

    }
}
*/
