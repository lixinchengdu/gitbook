# 139. Word Break

* *Difficulty: Medium*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Word Break II](word-break-ii.md)

## Problem:

<p>Given a <strong>non-empty</strong> string <em>s</em> and a dictionary <em>wordDict</em> containing a list of <strong>non-empty</strong> words, determine if <em>s</em> can be segmented into a space-separated sequence of one or more dictionary words.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The same word in the dictionary may be reused multiple times in the segmentation.</li>
	<li>You may assume the dictionary does not contain duplicate words.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, wordDict = [&quot;leet&quot;, &quot;code&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because <code>&quot;leetcode&quot;</code> can be segmented as <code>&quot;leet code&quot;</code>.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;applepenapple&quot;, wordDict = [&quot;apple&quot;, &quot;pen&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because <code>&quot;</code>applepenapple<code>&quot;</code> can be segmented as <code>&quot;</code>apple pen apple<code>&quot;</code>.
&nbsp;            Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;catsandog&quot;, wordDict = [&quot;cats&quot;, &quot;dog&quot;, &quot;sand&quot;, &quot;and&quot;, &quot;cat&quot;]
<strong>Output:</strong> false
</pre>

## Solutions:

```c++
class Solution {
public:
    struct TrieNode{
        bool stop;
        TrieNode* next[26];
        TrieNode(bool stop = false) {
            this->stop = stop;
            for (int i = 0; i < 26; ++i) {
                next[i] = nullptr;
            }
        }
    };
    
    class Trie {
        public:
            Trie() {
                root = new TrieNode();
                cur = root;
            }
        
            TrieNode* getCur() {
                return cur;
            }
        
            void setCur(TrieNode* cur) {
                this->cur = cur;
            }
        
            void rewind() {
                cur = root;
            }
        
            bool next(char c) {
                if (cur == nullptr || cur->next[c - 'a'] == nullptr) {
                    cur = nullptr;
                    return false;
                }
                
                cur = cur->next[c - 'a'];
                return true;
            }
        
            bool isWord() {
                return cur->stop;
            }
        
            void input(string s) {
                cur = root;
                for (auto c : s) {
                    if (cur->next[c - 'a'] == nullptr) {
                        cur->next[c - 'a'] = new TrieNode();
                    }
                    cur = cur->next[c - 'a'];
                }
                cur->stop = true;
                cur = root;
            }
        private:
            TrieNode* root;
            TrieNode* cur;
    };
    
    
    bool wordBreak(string s, vector<string>& wordDict) {
        Trie trie;
        for (auto word : wordDict) {
            trie.input(word);
        }
        
        unordered_map<int, bool> cache;
        
        return helper(s, 0, trie, cache);
    }
    
    bool helper(const string& s, int pos, Trie& trie, unordered_map<int, bool>& cache) {
        if (pos == s.length())  return true;
        if (cache.count(pos) > 0)   return cache[pos];
        for (int i = pos; i < s.length(); ++i) {
            if (trie.next(s[i]) == false) {
                cache[pos] = false;
                return false;
            } else {
                if (trie.isWord()) {
                    TrieNode* cur = trie.getCur();
                    trie.rewind();
                    if (helper(s, i + 1, trie, cache)) {
                        cache[pos] = true;
                        return true;
                    }
                    trie.setCur(cur);
                }
            }
        }
        cache[pos] = false;
        return false;
    }
    
    
};
```
