class Solution {
  public int countHomogenous(String s) {
    char prev = '?';
    int cnt = 1;
    int sum = 0;

    for(int i = 0; i < s.length(); ++i) {
        char c = s.charAt(i);
        if (c != prev) {
            cnt = 1;
            prev = c;
        }
        sum = (sum + cnt++) % 1000000007;
    }

    // for (char c : s.toCharArray()) {
    //   if (c != prev) {
    //     cnt = 1;
    //     prev = c;
    //   }
    //   sum = (sum + cnt++) % 1000000007;
    // }
    return sum;
  }
}
