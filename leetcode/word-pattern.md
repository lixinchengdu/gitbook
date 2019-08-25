# 290. Word Pattern

* *Difficulty: Easy*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Isomorphic Strings](isomorphic-strings.md)

  * [Word Pattern II](word-pattern-ii.md)

## Problem:

<p>Given a <code>pattern</code> and a string <code>str</code>, find if <code>str</code> follows the same pattern.</p>

<p>Here <b>follow</b> means a full match, such that there is a bijection between a letter in <code>pattern</code> and a <b>non-empty</b> word in <code>str</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> pattern = <code>&quot;abba&quot;</code>, str = <code>&quot;dog cat cat dog&quot;</code>
<strong>Output:</strong> true</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>pattern = <code>&quot;abba&quot;</code>, str = <code>&quot;dog cat cat fish&quot;</code>
<strong>Output:</strong> false</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> pattern = <code>&quot;aaaa&quot;</code>, str = <code>&quot;dog cat cat dog&quot;</code>
<strong>Output:</strong> false</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> pattern = <code>&quot;abba&quot;</code>, str = <code>&quot;dog dog dog dog&quot;</code>
<strong>Output:</strong> false</pre>

<p><b>Notes:</b><br />
You may assume <code>pattern</code> contains only lowercase letters, and <code>str</code> contains lowercase letters that may be separated by a single space.</p>

## Solutions:

```c++
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        unordered_map<char, string> patternToString;
        unordered_map<string, char> stringToPattern;
        
        int pos = 0;
        for (int i = 0; i < pattern.length(); ++i) {
            char c = pattern[i];
            string sub;
            while (pos < str.length() && str[pos] != ' ') {
                sub.push_back(str[pos]);
                ++pos;
            }
            
            if (patternToString.count(c) == 0 && stringToPattern.count(sub) == 0) {
                patternToString[c] = sub;
                stringToPattern[sub] = c;
            } else {
                if (sub != patternToString[c] || c != stringToPattern[sub]) return false;
            }
            
            if (pos == str.length()) {
                return i == pattern.length() - 1;
            }
            
            ++pos;
        }
        return false;
    }
};
```
