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
        if (strs.empty())   return ret;   
        int i = 0;
        while (true) {
            if (i >= strs[0].length())  return ret;
            char commonChar = strs[0][i];
            for (auto& str : strs) {
                if (i >= str.length() || commonChar != str[i])  return ret;
            }
            ret.push_back(commonChar);
            ++i;
        }
    }
};
```
