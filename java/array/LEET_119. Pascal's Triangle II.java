class Solution {
    
    public List<Integer> getRow(int rowIndex) {

        List<Integer> prev = new ArrayList<Integer>();

        prev.add(1);

        for(int i=0;i< rowIndex; i++){

            List<Integer> pres = new ArrayList<Integer>();
            pres.add(1);

            for(int j=1;j < prev.size(); j++)
                pres.add(j, prev.get(j)+prev.get(j-1));
                
            pres.add(1);
            prev = pres;
        }
        return prev;
    }
}
