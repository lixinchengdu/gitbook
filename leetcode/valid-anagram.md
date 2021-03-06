# 242. Valid Anagram

* *Difficulty: Easy*

* *Topics: Hash Table, Sort*

* *Similar Questions:*

  * [Group Anagrams](group-anagrams.md)

  * [Palindrome Permutation](palindrome-permutation.md)

  * [Find All Anagrams in a String](find-all-anagrams-in-a-string.md)

## Problem:

<p>Given two strings <em>s</em> and <em>t&nbsp;</em>, write a function to determine if <em>t</em> is an anagram of <em>s</em>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <em>s</em> = &quot;anagram&quot;, <em>t</em> = &quot;nagaram&quot;
<b>Output:</b> true
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <em>s</em> = &quot;rat&quot;, <em>t</em> = &quot;car&quot;
<b>Output: </b>false
</pre>

<p><strong>Note:</strong><br />
You may assume the string contains only lowercase alphabets.</p>

<p><strong>Follow up:</strong><br />
What if the inputs contain unicode characters? How would you adapt your solution to such case?</p>

## Solutions:

```c++
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())   return false;
        int count[26] = {0};
        for (auto c : s) {
            ++count[c - 'a'];
        }
        
        for (auto c : t) {
            if (--count[c - 'a'] < 0) return false; 
        }
        
        return true;
    }
};
```
