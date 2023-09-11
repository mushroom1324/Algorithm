class Pair {
    public String word;
    public int cnt;

    Pair (String word, int cnt) {
        this.word = word;
        this.cnt = cnt;
    }
}

class Solution {

    private Queue<Pair> queue = new ArrayDeque<>();
    private HashSet<String> set = new HashSet<>();
    private int len;

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        len = beginWord.length();

        queue.add(new Pair(beginWord, 1));

        toHashSet(wordList);

        set.remove(beginWord);

        while(!queue.isEmpty()) {
            Pair cur = queue.poll();

            if (cur.word.equals(endWord)) return cur.cnt;

            for (int i = 0; i < len; ++i) {
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    char charArr[] = cur.word.toCharArray();
                    charArr[i] = ch;

                    String str = new String(charArr);

                    if (set.contains(str)) {
                        set.remove(str);
                        queue.add(new Pair(str, cur.cnt + 1));
                    }
                }   
            }
        }

        return 0;
    }

    private void toHashSet(List<String> wordList) {
        for (int i = 0; i < wordList.size(); ++i) 
            set.add(wordList.get(i));
    }
}
