class Solution {
    public int firstMissingPositive(int[] nums) {

        int n = nums.length;

        // Step 1: Perform cyclic sort to arrange positive integers in their correct positions
        for (int i = 0; i < n; ++i) {
            while (nums[i] > 0 && nums[i] <= n 
            && nums[i] != nums[nums[i] - 1]) {
                swap(nums, i, nums[i] - 1);
            }
        }

        // Step 2: Find the first missing positive integer
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        // If all positive integers are present, return the next positive integer
        return n + 1;
        
    }

    static void swap(int[] nums, int first, int second) {
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
    }
}

/*
==== PREVIOUS SOLUTION ====
Time : 30.6% Memory : 6.07%

class Solution {
    public int firstMissingPositive(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for (int each : nums) {
            if (each > 0) set.add(each);
        }

        int i = 1;

        while(true) {
            
            if (!set.contains(i++)) return --i;
            
        }
   
    }
}
*/
