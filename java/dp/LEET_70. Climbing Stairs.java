/*
class Solution {
    public int climbStairs(int n) {

        return helper(n);
        
    }

    private int helper(int n) {
        
        if (n == 0 || n == 1) return 1;
        return helper(n - 1) + helper(n - 2);

    }
}
*/
class Solution {

    private Map<Integer, Integer> hashMap = new HashMap<>();

    public int climbStairs(int n) {

        return helper(n);
        
    }

    private int helper(int n) {
        
        if (n == 0 || n == 1) return 1;

        if (!hashMap.containsKey(n)) hashMap.put(n, helper(n - 1) + helper(n - 2));

        return hashMap.get(n);
    }
}
