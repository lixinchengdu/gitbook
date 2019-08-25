# 76. Minimum Window Substring

* *Difficulty: Hard*

* *Topics: Hash Table, Two Pointers, String, Sliding Window*

* *Similar Questions:*

  * [Substring with Concatenation of All Words](substring-with-concatenation-of-all-words.md)

  * [Minimum Size Subarray Sum](minimum-size-subarray-sum.md)

  * [Sliding Window Maximum](sliding-window-maximum.md)

  * [Permutation in String](permutation-in-string.md)

  * [Smallest Range Covering Elements from K Lists](smallest-range-covering-elements-from-k-lists.md)

  * [Minimum Window Subsequence](minimum-window-subsequence.md)

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
        unordered_map<char, int> charCount;
        for (auto c : t) {
            ++charCount[c];
        }
        
        int r = 0;
        int l = 0;
        int count = t.length();
        string ret;
        int len = INT_MAX;
        
        
        for (r = 0; r < s.length(); ++r) {
            char c = s[r];
            if (charCount.count(c) == 0) continue;
            --charCount[c];
            if (charCount[c] >= 0)  --count;
            if (charCount[c] == 0 && count == 0) {  
                while (true) {
                    if (charCount.count(s[l]) == 0) {
                        ++l;
                    } else {
                        char lastC = s[l];
                        ++l;
                        ++charCount[lastC];
                        if (charCount[lastC] == 1) {
                            ++count;
                            break;
                        }
                    }
                }
                
                if (r - l + 2 < len) {
                    len = r - l + 2;
                    ret = s.substr(l-1, len);
                }
            }
        }
        
        return len == INT_MAX ? "" : ret;
    }
};
```
