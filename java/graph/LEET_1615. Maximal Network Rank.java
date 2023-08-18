class Solution {

    private int[][] roads;
    private HashMap<Integer, List<Integer>> hm = new HashMap<>();

    public int maximalNetworkRank(int n, int[][] roads) {
        this.roads = roads;
        makeHashMap();
        
        int maxRank = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                maxRank = Math.max(findRank(i, j), maxRank);
            }
        }

        return maxRank;
    }
    
    private int findRank(int i, int j) {
        int rank = hm.getOrDefault(i, new ArrayList<>()).size() + 
                   hm.getOrDefault(j, new ArrayList<>()).size();

        if (hm.getOrDefault(i, new ArrayList<>()).contains(j)) {
            rank--; 
        }

        return rank;
    }

    private void makeHashMap() {
        for (int[] each : roads) {
            hm.putIfAbsent(each[0], new ArrayList<>());
            hm.putIfAbsent(each[1], new ArrayList<>());
            hm.get(each[0]).add(each[1]);
            hm.get(each[1]).add(each[0]);
        }
    }
}
