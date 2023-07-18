class Solution { // 50%
    public int majorityElement(int[] nums) {

        Arrays.sort(nums);
        return nums[nums.length/2];

    }
}

class Solution { // 45%
    public int majorityElement(int[] nums) {

        Arrays.sort(nums);

        int prev = nums[0];
        int cnt = 1;

        for(int i = 1; i < nums.length; i++) {
            if (prev == nums[i]) cnt++;
            else cnt = 1;
            if (cnt > nums.length / 2) return nums[i];
            prev = nums[i];
        }

        return nums[0];

    }
}

class Solution2 { // 28%
    public int majorityElement(int[] nums) {

        Map<Integer, Integer> hash = new HashMap<>();

        for (int num : nums) {
            int cur = hash.getOrDefault(num, 0) + 1;
            if (cur > nums.length / 2) return num;
            hash.put(num, cur);
        }

        return 0;
    }
}