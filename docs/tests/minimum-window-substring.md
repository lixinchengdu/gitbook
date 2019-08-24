# 76. Minimum Window Substring

* *Difficulty: Hard*

* *Topics: Hash Table, Two Pointers, String, Sliding Window*

* *Similar Questions:*

  * [Substring with Concatenation of All Words](./tests/minimum-window-substring.md)

  * [Minimum Size Subarray Sum](./tests/minimum-window-substring.md)

  * [Sliding Window Maximum](./tests/minimum-window-substring.md)

  * [Permutation in String](./tests/minimum-window-substring.md)

  * [Smallest Range Covering Elements from K Lists](./tests/minimum-window-substring.md)

  * [Minimum Window Subsequence](./tests/minimum-window-substring.md)

## Problem:

<p>Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: S</strong> = &quot;ADOBECODEBANC&quot;, <strong>T</strong> = &quot;ABC&quot;
<strong>Output:</strong> &quot;BANC&quot;
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>If there is no such window in S that covers all characters in T, return the empty string <code>&quot;&quot;</code>.</li>
	<li>If there is such window, you are guaranteed that there will always be only one unique minimum window in S.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    string minWindow(string s, string t) {
        string result;
        int minLen = INT_MAX;
        int start = 0, end = 0;
        map <char, int> charCount;
        for (auto c: t)
        {
            charCount[c] ++;
        }
        int existCharNum = charCount.size();
        if (existCharNum == 0)  return result;
        for (end = 0; end < s.length(); end++)
        {
            if (charCount.find(s[end]) != charCount.end())
            {
                if ((--charCount[s[end]]) == 0) existCharNum--;
                if (existCharNum == 0)
                {
                    while (existCharNum == 0 && start <= end)
                    {
                        if (charCount.find(s[start]) != charCount.end())
                        {
                            if (charCount[s[start]] ++ == 0)
                                existCharNum ++;
                        }
                        start++;
                    }
                    if (existCharNum != 0)
                    {
                        if (end - start + 2 < minLen)
                        {
                            minLen = end-start+2;
                            result = s.substr(start-1, minLen);
                        }
                    }
                }
            }
        }
        return result;
    }
};
```
