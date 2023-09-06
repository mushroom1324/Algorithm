class Solution {

    private HashMap<Integer,Integer> map = new HashMap<>();

    public List<Integer> majorityElement(int[] nums) {
        
        for (int each : nums) 
            map.put(each, map.getOrDefault(each, 0) + 1);

        List<Integer> ans = new ArrayList<>();

        for(int each : map.keySet()){
            if ( map.get(each) > nums.length / 3 )
                ans.add(each);
        }

        return ans;
    }
}   
