// DP approach
// dp always works if possible btw

class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        int[][] dp = new int[m + 1][n + 1];
        
        // root case : init first line to 1
        for (int i = 0; i <= m; i++) dp[i][0] = 1; 
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j];
            }
        }
        
        return dp[m][n];
    }
}


// BFS approach : TLE

// class Pair {
//     int index;
//     int target;

//     public Pair(int index, int target) {
//         this.index = index;
//         this.target = target;
//     }
// }

// class Solution {
//     public int numDistinct(String s, String t) {
//         // iterate each char and check for:
//         // each == target
//         //
//         // add to queue with each + 1, target
//         // if true, add to queue, each + 1, target + 1
//         // 
//         // if target == t.length, cnt++

//         int cnt = 0;

//         Queue<Pair> q = new LinkedList<>();

//         q.add(new Pair(0, 0));

//         while (!q.isEmpty()) {
//             Pair cur = q.poll();

//             if (s.charAt(cur.index) == t.charAt(cur.target)) {
//                 if (cur.target == t.length() - 1) cnt++;
//                 else q.add(new Pair(cur.index + 1, cur.target + 1));
//             }

//             if (cur.index < s.length() - 1) 
//                 q.add(new Pair(cur.index + 1, cur.target));

//         }

//         return cnt;

//     }
// }
