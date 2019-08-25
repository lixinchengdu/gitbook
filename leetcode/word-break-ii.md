# 140. Word Break II

* *Difficulty: Hard*

* *Topics: Dynamic Programming, Backtracking*

* *Similar Questions:*

  * [Word Break](word-break.md)

  * [Concatenated Words](concatenated-words.md)

## Problem:

<p>Given a <strong>non-empty</strong> string <em>s</em> and a dictionary <em>wordDict</em> containing a list of <strong>non-empty</strong> words, add spaces in <em>s</em> to construct a sentence where each word is a valid dictionary word.&nbsp;Return all such possible sentences.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The same word in the dictionary may be reused multiple times in the segmentation.</li>
	<li>You may assume the dictionary does not contain duplicate words.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong>s = &quot;<code>catsanddog</code>&quot;
wordDict = <code>[&quot;cat&quot;, &quot;cats&quot;, &quot;and&quot;, &quot;sand&quot;, &quot;dog&quot;]</code>
<strong>Output:
</strong><code>[
&nbsp; &quot;cats and dog&quot;,
&nbsp; &quot;cat sand dog&quot;
]</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
</strong>s = &quot;pineapplepenapple&quot;
wordDict = [&quot;apple&quot;, &quot;pen&quot;, &quot;applepen&quot;, &quot;pine&quot;, &quot;pineapple&quot;]
<strong>Output:
</strong>[
&nbsp; &quot;pine apple pen apple&quot;,
&nbsp; &quot;pineapple pen apple&quot;,
&nbsp; &quot;pine applepen apple&quot;
]
<strong>Explanation:</strong> Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:
</strong>s = &quot;catsandog&quot;
wordDict = [&quot;cats&quot;, &quot;dog&quot;, &quot;sand&quot;, &quot;and&quot;, &quot;cat&quot;]
<strong>Output:
</strong>[]</pre>

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
        
            TrieNode* getRoot() {
                return root;
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
    
    
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        Trie trie;
        for (auto word : wordDict) {
            trie.input(word);
        }
        
        unordered_map<int, vector<vector<string>>> cache;
        
        auto wordLists = helper(s, 0, trie, cache);
        vector<string> ret;
        for (auto& wordList : wordLists) {
            ret.push_back(join(wordList));
        }
        return ret;
    }
    
    string join(const vector<string>& path) {
        string s;
        if (path.size() == 0)   return s;
        s = path[0];
        for (int i = 1; i < path.size(); ++i) {
            s.append(" ");
            s.append(path[i]);
        }
        return s;
    }
    
    vector<vector<string>> helper(const string& s, int pos, Trie& trie, unordered_map<int, vector<vector<string>>>& cache) {
        vector<vector<string>> ret;
        if (cache.count(pos) > 0) {
            return cache[pos];
        }
        for (int j = pos; j < s.length(); ++j) {
            if (!trie.next(s[j])) {
               break;
            } else {
                if (trie.isWord()) {
                    if (j == s.length() - 1){
                        ret.push_back({s.substr(pos)});       
                    }
                    TrieNode* cur = trie.getCur();
                    trie.rewind();
                    auto suffix = helper(s, j + 1, trie, cache);
                    trie.setCur(cur);
                    for (auto& path : suffix) {
                        ret.push_back({s.substr(pos, j - pos + 1)});
                        ret.back().insert(ret.back().end(), path.begin(), path.end());
                    }
                }
            }
        }
        cache[pos] = ret;
        return ret;
    }
};
```
