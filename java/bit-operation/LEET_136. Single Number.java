class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0; 
        
        for(int i = 0; i < nums.length; ++i)
            ans ^= nums[i];  // XOR 두번 때리면 없어짐
        
        return ans; // 하나만 있는 원소 반환  
    }
}
