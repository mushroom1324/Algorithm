class Solution {

    public List<String> buildArray(int[] target, int n) {        
        List<String> ans = new ArrayList<>();
        int cur = 1;

        for(int i = 0; i < target.length; ++i) {

            while(cur != target[i]) {
                ans.add("Push");
                ans.add("Pop");
                ++cur;
            }   
            ans.add("Push");
            ++cur;
        }
        
        return ans;
    }
}
