class Solution {

    int[] dp;

    public int jump(int[] nums) {
        int n = nums.length;
        dp = new int[n];
        Arrays.fill(dp, -1);

        dp[0] = 0;

        // iterate
        for (int i = 0; i < n; ++i) {
            for(int j = 1; j <= nums[i]; ++j) {

                // break when j is over n
                if (i + j >= n) break;

                // if not visited
                if (dp[i + j] == -1) dp[i + j] = dp[i] + 1;

                // if visited, set the minimum value
                else dp[i + j] = Math.min(dp[i + j], dp[i] + 1);
            }
        }
        
        return dp[n - 1];
        
    }
}
