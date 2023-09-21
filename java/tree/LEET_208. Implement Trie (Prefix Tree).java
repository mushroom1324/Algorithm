class TrieNode {
    boolean isWord;
    TrieNode[] children;

    public TrieNode() {
        isWord = false;
        children = new TrieNode[26];
    }
}

class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {

        TrieNode node = root;

        for (char each : word.toCharArray()) {
            if (node.children[each - 'a'] == null) node.children[each - 'a'] = new TrieNode();
            node = node.children[each - 'a'];
        }

        node.isWord = true;
        
    }
    
    public boolean search(String word) {

        TrieNode node = root;

        for(char each : word.toCharArray()) {
            if (node.children[each - 'a'] == null) return false;
            node = node.children[each - 'a'];
        }
        return node.isWord;
    
    }
    
    public boolean startsWith(String prefix) {

        TrieNode node = root;

        for(char each : prefix.toCharArray()) {
            if (node.children[each - 'a'] == null) return false;
            node = node.children[each - 'a'];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

//  class Trie {

//     private List<String> arr;

//     public Trie() {
//         this.arr = new ArrayList<>();
//     }
    
//     public void insert(String word) {
//         arr.add(word);
//     }
    
//     public boolean search(String word) {
//         return arr.contains(word);
//     }
    
//     public boolean startsWith(String prefix) {
//         boolean ans = false;
//         for (String each : arr) {
//             if (prefix.length() > each.length()) continue;
//             if (each.substring(0, prefix.length()).equals(prefix)) ans = true;
//         }
            
        
//         return ans;
//     }
// }
