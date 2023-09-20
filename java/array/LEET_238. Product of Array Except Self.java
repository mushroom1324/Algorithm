class Solution {
    private int temp;
    private int cnt;
    private int[] ans;
    private int index;

    public int[] productExceptSelf(int[] nums) {
        ans = new int[nums.length];
        temp = 1;

        for(int i = 0; i < nums.length; ++i) {
            if (nums[i] == 0) {
                ++cnt;
                index = i;
            }
            else temp *= nums[i];
        }

        if (cnt > 1) return ans;

        if (cnt == 1) {
            ans[index] = temp;
            return ans;
        }

        for (int i = 0; i < nums.length; ++i) {
            ans[i] = temp / nums[i];
        }
        return ans;

        

        

    }
}
