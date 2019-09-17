# 1129. Longest String Chain

* *Difficulty: Medium*

* *Topics: Hash Table, Dynamic Programming*

* *Similar Questions:*

## Problem:

<p>Given a list of words, each word consists of English lowercase letters.</p>

<p>Let&#39;s say <code>word1</code> is a predecessor of <code>word2</code>&nbsp;if and only if we can add exactly one letter anywhere in <code>word1</code> to make it equal to <code>word2</code>.&nbsp; For example,&nbsp;<code>&quot;abc&quot;</code>&nbsp;is a predecessor of <code>&quot;abac&quot;</code>.</p>

<p>A <em>word chain&nbsp;</em>is a sequence of words <code>[word_1, word_2, ..., word_k]</code>&nbsp;with <code>k &gt;= 1</code>,&nbsp;where <code>word_1</code> is a predecessor of <code>word_2</code>, <code>word_2</code> is a predecessor of <code>word_3</code>, and so on.</p>

<p>Return the longest possible length of a word chain with words chosen from the given list of <code>words</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;a&quot;,&quot;b&quot;,&quot;ba&quot;,&quot;bca&quot;,&quot;bda&quot;,&quot;bdca&quot;]</span>
<strong>Output: </strong><span id="example-output-1">4
<strong>Explanation</strong>: one of </span>the longest word chain is &quot;a&quot;,&quot;ba&quot;,&quot;bda&quot;,&quot;bdca&quot;.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 16</code></li>
	<li><code>words[i]</code> only consists of English lowercase letters.</li>
</ol>

<div>
<p>&nbsp;</p>
</div>
## Solutions:

```c++
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        if (words.size() == 0)  return 0;
        auto comparator = [](const string& word1, const string& word2) {
            return word1.length() < word2.length();
        };
        
        int ret = 0;
        unordered_map<string, int> dp = {};
        sort(words.begin(), words.end(), comparator);
        int pos = 0;
        for (int len = 1; len <= words.back().length(); ++len) {
            unordered_map<string, int> temp;
            while (pos < words.size() && words[pos].length() == len) {
                string word = words[pos];
                temp[word] = 1; // this initializaiton is very important!
                for (auto& entry : dp) {
                    if (isPredecessor(entry.first, word)) {
                        temp[word] = max(temp[word], 1 + entry.second);
                    }
                }
                ret = max(ret, temp[word]);
                // update pos
                ++pos;
            }
            swap(dp, temp);
        }
        
        return ret;
    }
    
private:
    bool isPredecessor(const string& str1, const string& str2) {
        int pos = 0;
        while (pos < str1.length() && str1[pos] == str2[pos]) ++pos;
        if (pos == str1.length())   return true;
        while (pos < str1.length() && str1[pos] == str2[pos + 1]) ++pos;
        return pos == str1.length();
    }
    
};
```
