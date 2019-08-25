# 208. Implement Trie (Prefix Tree)

* *Difficulty: Medium*

* *Topics: Design, Trie*

* *Similar Questions:*

  * [Add and Search Word - Data structure design](add-and-search-word-data-structure-design.md)

  * [Design Search Autocomplete System](design-search-autocomplete-system.md)

  * [Replace Words](replace-words.md)

  * [Implement Magic Dictionary](implement-magic-dictionary.md)

## Problem:

<p>Implement a trie with <code>insert</code>, <code>search</code>, and <code>startsWith</code> methods.</p>

<p><b>Example:</b></p>

<pre>
Trie trie = new Trie();

trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // returns true
trie.search(&quot;app&quot;);     // returns false
trie.startsWith(&quot;app&quot;); // returns true
trie.insert(&quot;app&quot;);   
trie.search(&quot;app&quot;);     // returns true
</pre>

<p><b>Note:</b></p>

<ul>
	<li>You may assume that all inputs are consist of lowercase letters <code>a-z</code>.</li>
	<li>All inputs are guaranteed to be non-empty strings.</li>
</ul>

## Solutions:

```c++
class Trie {
public:
    struct TrieNode{
        bool isWord;
        TrieNode* next[26];
        TrieNode(bool isWord = false) {
            this->isWord = isWord;
            for (int i = 0; i < 26; ++i) {
                next[i] = nullptr;
            }
        }
    };
    
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode(false);
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* lastNode = findNode(word, true);
        lastNode->isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* lastNode = findNode(word, false);
        return lastNode != nullptr && lastNode->isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return findNode(prefix, false) != nullptr;
    }
private:
    TrieNode* findNode(string& word, bool modifiable) {
        TrieNode* cur = root;
        for (auto& c : word) {
            if (cur->next[c - 'a'] == nullptr) {
                if (!modifiable)    return nullptr;
                cur->next[c -'a'] = new TrieNode(false);
            }
            cur = cur->next[c - 'a'];
        }
        return cur;
    }
    
    TrieNode* root;  
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```
