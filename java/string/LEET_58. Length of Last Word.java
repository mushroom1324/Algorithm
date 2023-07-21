class Solution {
    public int lengthOfLastWord(String s) {
        int length = s.length() - 1;

        while(length >= 0 && s.charAt(length) == ' ') {
            length--;
        }

        int cnt = 0;

        while(length >= 0 && s.charAt(length) != ' ') {
            length--;
            cnt++;
        }

        return cnt;

    }
}