class Solution {
    public boolean canJump(int[] nums) {
        int reachable = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (i > reachable) return false;
            reachable = Math.max(reachable, i + nums[i]);
        }
        return true;
    }
}

// previous solution : dp
//
// class Solution {
//     public boolean canJump(int[] nums) {
//         int n = nums.length;
//         if (n == 1) return true;
//         boolean[] dp = new boolean[n];

//         Arrays.fill(dp, false);
//         dp[0] = true;

//         for (int i = 0; i < n - 1; ++i) {
//             for (int j = 1;dp[i] && j <= nums[i] && i + j < n; ++j) {
//                 dp[i + j] = true;
//             }
//         }
//         return dp[n - 1];
//     }
// }
