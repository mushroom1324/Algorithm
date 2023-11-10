class Solution {
    public int largestAltitude(int[] gain) {

        int maxVal = 0;
        int cur = 0;

        for (int i = 0; i < gain.length; i++) {
            cur += gain[i]; {
                maxVal = Math.max(maxVal, cur);
            }
        }
        
        return maxVal;        
    }
}
