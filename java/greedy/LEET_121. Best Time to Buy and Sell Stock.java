class Solution {

    public int maxProfit(int[] prices) {
        int maxVal = 0;
        int minPrice = prices[0];

        for (int i = 0; i < prices.length; i++) {
            minPrice = Math.min(prices[i], minPrice);
            int profit = prices[i] - minPrice;
            maxVal = Math.max(maxVal, profit);
        }
        return maxVal;
    }
}