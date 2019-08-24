# 211. Add and Search Word - Data structure design

* *Difficulty: Medium*

* *Topics: Backtracking, Design, Trie*

* *Similar Questions:*

  * [Implement Trie (Prefix Tree)](./tests/add-and-search-word-data-structure-design.md)

  * [Prefix and Suffix Search](./tests/add-and-search-word-data-structure-design.md)

## Problem:

<p>Design a data structure that supports the following two operations:</p>

<pre>
void addWord(word)
bool search(word)
</pre>

<p>search(word) can search a literal word or a regular expression string containing only letters <code>a-z</code> or <code>.</code>. A <code>.</code> means it can represent any one letter.</p>

<p><strong>Example:</strong></p>

<pre>
addWord(&quot;bad&quot;)
addWord(&quot;dad&quot;)
addWord(&quot;mad&quot;)
search(&quot;pad&quot;) -&gt; false
search(&quot;bad&quot;) -&gt; true
search(&quot;.ad&quot;) -&gt; true
search(&quot;b..&quot;) -&gt; true
</pre>

<p><b>Note:</b><br />
You may assume that all words are consist of lowercase letters <code>a-z</code>.</p>

## Solutions:

```c++
class WordDictionary {
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new TrieNode;
        memset(root -> nextTrieNode, NULL, sizeof(TrieNode*) * 26);
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        addWordHelper (word, root);
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return searchHelper (word, root);
    }   
        
    ~WordDictionary()
    {
        deleteHelper (root);
    }
    
private:
    struct TrieNode
    {
        char c;
        struct TrieNode* nextTrieNode[26];
    };
    
    typedef struct TrieNode TrieNode;
    
    TrieNode* root;
    
    void deleteHelper (TrieNode* root)
    {   
        if (!root)  return;
        for (int i = 0; i < 26; i++)    deleteHelper (root->nextTrieNode[i]);
        delete root;
    }
    
    bool searchHelper (string suffix, TrieNode* root)
    {
        //cout << suffix << endl;
        if (suffix.length() == 0 && root->c == '#')
        {
            return true;
        }
        
        if (suffix.length() == 0)  return false;
        else
        {
            if (suffix[0] != '.')
            {
                if (root -> nextTrieNode[suffix[0] - 'a'])   return searchHelper (suffix.substr(1), root -> nextTrieNode[suffix[0]- 'a']);
                else return false;
            }
            else
            {
                for (int i =0; i < 26; i++)
                {
                    if (root -> nextTrieNode[i] && searchHelper (suffix.substr(1), root -> nextTrieNode[i]))  return true;
                }
                return false;
            }
        }
    }
    
    void addWordHelper (string suffix, TrieNode* root)
    {
        if (suffix.length() == 0)   {root -> c = '#'; return;}
        if (root -> nextTrieNode[suffix[0]-'a'])    addWordHelper(suffix.substr(1), root -> nextTrieNode[suffix[0]-'a']);
        else
        {
            root -> nextTrieNode[suffix[0]-'a'] = new TrieNode;
            memset(root -> nextTrieNode[suffix[0]-'a'] -> nextTrieNode, NULL, sizeof(TrieNode*) * 26);
            addWordHelper (suffix.substr(1), root -> nextTrieNode[suffix[0]-'a']);
        }
    }
    
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * bool param_2 = obj.search(word);
 */
```
