class Solution {
    public int getWinner(int[] arr, int k) {

        if (k > arr.length) {
            int ans = -999999999;
            for (int each : arr) {
                ans = Math.max(ans, each);
            }
            return ans;
        }
        
        Deque<Integer> q = new ArrayDeque<>();

        for (int each : arr) {
            q.add(each);
        }

        int cnt = 0;
        int prev = q.poll();

        while (cnt != k) {
            
            int cur = q.poll();

            if (prev > cur) {
                ++cnt;
                q.add(cur);
            }
            else {
                cnt = 1;
                q.add(prev);
                prev = cur;
            }
        }
        return prev;

    }
}
