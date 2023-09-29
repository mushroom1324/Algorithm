class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> hm = new HashMap<>();

        for (String each : words) {
            hm.put(each, hm.getOrDefault(each, 0) + 1);
        }

        List<String> keySet = new ArrayList<>(hm.keySet());

        keySet.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                int v1 = hm.get(o1);
                int v2 = hm.get(o2);
                if (v1 == v2) {    
                    // if same value..
                    return o1.compareTo(o2); 
                }

                return Integer.compare(v2, v1);
            }
        });
        
        return keySet.subList(0, k);
    }
}
