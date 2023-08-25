class Solution {

    private int[] dp;
    private int[] nums;

    public int rob(int[] nums) { 
        this.nums = nums;     
        int n = nums.length;

        // base cases
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);

        dp = new int[n];
        Arrays.fill(dp, -1);

        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for(int i = 2; i < n; ++i) {
            dp[i] = helper(i);
        }
        return dp[n - 1];
    }

    private int helper(int n) {
        // helper(n) = Math.max(helper(n - 2) + n, helper(n - 1))
        // if dp contains value, return its value
        if (dp[n] != -1) return dp[n];
        return Math.max(helper(n - 2) + nums[n], helper(n - 1));
        
    }
}
