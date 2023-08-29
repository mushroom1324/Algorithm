class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int i = 0; i < nums.length; ++i) {
            if (hm.getOrDefault(nums[i], 0) == 1) return true;
            hm.put(nums[i], 1);
        }
        return false;
    }
}
