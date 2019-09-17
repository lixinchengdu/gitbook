# 720. Longest Word in Dictionary

* *Difficulty: Easy*

* *Topics: Hash Table, Trie*

* *Similar Questions:*

  * [Longest Word in Dictionary through Deleting](longest-word-in-dictionary-through-deleting.md)

  * [Implement Magic Dictionary](implement-magic-dictionary.md)

## Problem:

<p>Given a list of strings <code>words</code> representing an English Dictionary, find the longest word in <code>words</code> that can be built one character at a time by other words in <code>words</code>.  If there is more than one possible answer, return the longest word with the smallest lexicographical order.</p>  If there is no answer, return the empty string.

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
words = ["w","wo","wor","worl", "world"]
<b>Output:</b> "world"
<b>Explanation:</b> 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
<b>Output:</b> "apple"
<b>Explanation:</b> 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
</pre>
</p>

<p><b>Note:</b>
<li>All the strings in the input will only contain lowercase letters.</li>
<li>The length of <code>words</code> will be in the range <code>[1, 1000]</code>.</li>
<li>The length of <code>words[i]</code> will be in the range <code>[1, 30]</code>.</li>
</p>
## Solutions:

```c++
class Solution {
public:
    string longestWord(vector<string>& words) {
        auto comparator = [](const string& word1, const string& word2) {
            if (word1.length() != word2.length()) {
                return word1.length() < word2.length();
            }  
            return word1 > word2;
        };
        
        sort(words.begin(), words.end(), comparator);
        unordered_set<string> cache;
        string ret;
        for (int i = 0; i < words.size(); ++i) {
            if (words[i].length() <= 1) {
                ret = words[i];
                cache.insert(words[i]);
                continue;
            }
            
            string prefix = words[i].substr(0, words[i].length() - 1);
            if (cache.count(prefix)) {
                ret = words[i];
                cache.insert(words[i]);
            }
        }
        
        return ret;
        
    }
};
```
