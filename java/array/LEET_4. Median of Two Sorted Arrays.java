class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // if (nums1 == null) {
        //     if (nums2.length % 2 == 1) {
        //         return (float) (nums2[nums2.length / 2] + nums2[nums2.length / 2 + 1]) / 2;
        //     }
        //     return nums2[nums2.length / 2];
        // }
        // if (nums2 == null) {
        //     if (nums1.length % 2 == 1) {
        //         return (float) (nums1[nums1.length / 2] + nums1[nums1.length / 2 + 1]) / 2;
        //     }
        //     return nums1[nums1.length / 2];
        // }



        int ptr1 = 0;
        int ptr2 = 0;

        int size = nums1.length + nums2.length;

        int[] nums3 = new int[size];
        int i = 0;

        while (ptr1 < nums1.length && ptr2 < nums2.length) {
            if (nums1[ptr1] < nums2[ptr2]) {
                nums3[i] = nums1[ptr1];
                ptr1++;
            } else {
                nums3[i] = nums2[ptr2];
                ptr2++;
            }
            i++;
        }

        while (ptr1 < nums1.length) {
            nums3[i] = nums1[ptr1];
            ptr1++;
            i++;
        }

        while (ptr2 < nums2.length) {
            nums3[i] = nums2[ptr2];
            ptr2++;
            i++;
        }

        if (size % 2 == 1) {
            return nums3[size / 2];
        }
        return (nums3[size / 2] + nums3[size / 2 - 1]) / 2.0;

    }
}