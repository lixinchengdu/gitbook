# 336. Palindrome Pairs

* *Difficulty: Hard*

* *Topics: Hash Table, String, Trie*

* *Similar Questions:*

  * [Longest Palindromic Substring](longest-palindromic-substring.md)

  * [Shortest Palindrome](shortest-palindrome.md)

## Problem:

<p>Given a list of <b>unique</b> words, find all pairs of <b><i>distinct</i></b> indices <code>(i, j)</code> in the given list, so that the concatenation of the two words, i.e. <code>words[i] + words[j]</code> is a palindrome.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;abcd&quot;,&quot;dcba&quot;,&quot;lls&quot;,&quot;s&quot;,&quot;sssll&quot;]</span>
<strong>Output: </strong><span id="example-output-1">[[0,1],[1,0],[3,2],[2,4]] 
<strong>E</strong></span><strong>xplanation<span>: </span></strong>The palindromes are <code>[&quot;dcbaabcd&quot;,&quot;abcddcba&quot;,&quot;slls&quot;,&quot;llssssll&quot;]</code>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;bat&quot;,&quot;tab&quot;,&quot;cat&quot;]</span>
<strong>Output: </strong><span id="example-output-2">[[0,1],[1,0]] 
</span><span id="example-output-1"><strong>E</strong></span><strong>xplanation<span>: </span></strong>The palindromes are <code>[&quot;battab&quot;,&quot;tabbat&quot;]</code>
</pre>
</div>
</div>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector<vector<int>> left = helper(words, true);
        vector<string> reverseWords;
        for (int i = 0; i < words.size(); ++i) {
            reverseWords.push_back({words[i].rbegin(), words[i].rend()});
        }
        vector<vector<int>> right = helper(reverseWords,false);
        set<vector<int>> ret;
        ret.insert(right.begin(), right.end());
        ret.insert(left.begin(), left.end());
        return vector<vector<int>>(ret.begin(), ret.end());
    }
    
    
    vector<vector<int>> helper(vector<string>& words, bool direction) {
        unordered_map<string, int> wordMap;
        for (int i = 0; i < words.size(); ++i) {
            wordMap[words[i]] = i;
        }
        
        vector<vector<int>> ret;
        for (int i = 0; i < words.size(); ++i) {
            string word = words[i];
            reverse(word.begin(), word.end());
            for (int j = word.length() - 1; j >= -1; --j) {   
                if (wordMap.count(word.substr(0, j + 1)) > 0 && isPalindrome(word.substr(j + 1, word.length() - j - 1))) {
                    if (i != wordMap[word.substr(0, j + 1)]) {
                        if (direction) // Two directions!!!
                            ret.push_back({wordMap[word.substr(0, j + 1)], i});
                        else 
                            ret.push_back({i, wordMap[word.substr(0, j + 1)]});
                        continue;
                    }
                }
            }
        }
        
        return ret;
    }
    
private:
    bool isPalindrome(string str) {
        //cout << str << endl;
        int left = 0;
        int right = str.length() - 1;
        while (left < right) {
            if (str[left] != str[right])    return false;
            ++left;
            --right;
        }
        return true;
    }
    
};
```
