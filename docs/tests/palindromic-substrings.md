# 647. Palindromic Substrings

* *Difficulty: Medium*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [Longest Palindromic Substring](./tests/palindromic-substrings.md)

  * [Longest Palindromic Subsequence](./tests/palindromic-substrings.md)

  * [Palindromic Substrings](./tests/palindromic-substrings.md)

## Problem:

<p>Given a string, your task is to count how many palindromic substrings in this string.</p>

<p>The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;abc&quot;
<b>Output:</b> 3
<b>Explanation:</b> Three palindromic strings: &quot;a&quot;, &quot;b&quot;, &quot;c&quot;.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;aaa&quot;
<b>Output:</b> 6
<b>Explanation:</b> Six palindromic strings: &quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;aa&quot;, &quot;aa&quot;, &quot;aaa&quot;.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The input string length won&#39;t exceed 1000.</li>
</ol>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    int countSubstrings(string s) {
        int ret = 0;
        for (int i = 0; i < s.length(); ++i) {
            ++ret;
            int radius = 1;
            while (i-radius >= 0 && i+radius < s.length() && s[i-radius] == s[i+radius]) {
                ++ret;
                ++radius;
            } 
            
            int left = i;
            int right = i + 1;
            while (left >=0 && right < s.length() && s[left--] == s[right++]) {
                ++ret;
            }
             
        }
        return ret;
    }
};
```
