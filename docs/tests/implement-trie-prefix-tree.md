# 208. Implement Trie (Prefix Tree)

* *Difficulty: Medium*

* *Topics: Design, Trie*

* *Similar Questions:*

  * [Add and Search Word - Data structure design](./tests/implement-trie-prefix-tree.md)

  * [Design Search Autocomplete System](./tests/implement-trie-prefix-tree.md)

  * [Replace Words](./tests/implement-trie-prefix-tree.md)

  * [Implement Magic Dictionary](./tests/implement-trie-prefix-tree.md)

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
    struct trieNode
    {
        bool isWord;
        trieNode* next[26];
        trieNode(bool b = false)
        {
            isWord = b;
            memset(next, 0, sizeof(next));
        }
    };

    /** Initialize your data structure here. */
    Trie() {
        root = new trieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        trieNode* cur = root;
        for (int i = 0; i < word.length(); i++)
        {
            if (cur->next[word[i]-'a'] != NULL)
            {
                cur = cur->next[word[i]-'a'];
            }
            else
            {
                cur->next[word[i]-'a'] = new trieNode();
                cur = cur->next[word[i]-'a'];
            }
        }
        cur->isWord = true;
        
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        trieNode* cur = root;
        for (int i = 0; i < word.length(); i++)
        {
            if (!cur->next[word[i]-'a'])    return false;
            cur = cur->next[word[i]-'a'];
        }
        return cur->isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        trieNode *cur = root;
        for (int i = 0; i < prefix.length(); i++)
        {
            if (!cur->next[prefix[i]-'a'])    return false;
            cur = cur->next[prefix[i]-'a'];
        }
        return true;
    }
    
    trieNode* root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * bool param_2 = obj.search(word);
 * bool param_3 = obj.startsWith(prefix);
 */
```
