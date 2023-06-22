/*

시간 100% 메모리 73%

*/

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0, i_m = 0, i_n = 0;
        int[] res = new int[m + n];
        while(i_m < m && i_n < n) {
            if(nums1[i_m] < nums2[i_n]) {
                res[i] = nums1[i_m];
                i_m++;
            }
            else {
                res[i] = nums2[i_n];
                i_n++;
            }
            i++;
        }
        while(i_n < n) {
            res[i] = nums2[i_n];
            i_n++;
            i++;
        }
        while(i_m < m) {
            res[i] = nums1[i_m];
            i_m++;
            i++;
        }

        i = 0;
        for(int each: res) {
            nums1[i] = each;
            i++;
        }
    }
}