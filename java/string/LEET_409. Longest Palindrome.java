class Solution {
    public int longestPalindrome(String s) {
        int length = 0;

        HashSet<Character> hashSet = new HashSet<Character>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (hashSet.contains(c)) {
                length += 2;
                hashSet.remove(c);
            }
            else {
                hashSet.add(c);
            }
        }

        if (hashSet.size() > 0) {
            length++;
        }

        return length;
    }
}
