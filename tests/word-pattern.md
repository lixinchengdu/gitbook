# 290. Word Pattern

* *Difficulty: Easy*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Isomorphic Strings](./tests/word-pattern.md)

  * [Word Pattern II](./tests/word-pattern.md)

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
#include <unordered_map>

class Solution {
public:
    bool wordPattern(string pattern, string str) {
        int StringIndex = 0;
        unordered_map <char, string> Pattern2String;
        unordered_map <string, char> String2Pattern;
        for (auto pattern_c : pattern)
        {
                if (StringIndex >= str.size())
                    return false;
                string TempString;
                while (StringIndex < str.size() && str[StringIndex] != ' ')
                {
                    TempString += str[StringIndex];
                    StringIndex ++;
                }
                StringIndex ++;
            
            if (Pattern2String.find (pattern_c) == Pattern2String.end())
            {
                Pattern2String [pattern_c] = TempString;
                if (String2Pattern.find(TempString) == String2Pattern.end())
                    String2Pattern [TempString] = pattern_c;
                else
                    return false;
            }
            else
            {
                if (Pattern2String[pattern_c] != TempString)
                    return false;
            }
        }
        
        if ( StringIndex == str.size()+1 )
            return true;
        else
            return false;
        
    }
};
```
