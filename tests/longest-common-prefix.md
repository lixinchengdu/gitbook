# 14. Longest Common Prefix

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p><strong>Note:</strong></p>

<p>All given inputs are in lowercase letters <code>a-z</code>.</p>

## Solutions:

```c++
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ret;
        int pos = 0;
        if (strs.size() == 0)   return ret;
        
        for (int pos = 0; pos < strs[0].length(); ++pos) {
            char c = strs[0][pos];
            for (auto& str: strs) {
                if (str.length() == pos)    return ret;
                if (str[pos] != c)  return ret;
            }
            ret.push_back(c);
        }
        return ret;
    }
};
```
