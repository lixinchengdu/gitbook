# 647. Palindromic Substrings

* *Difficulty: Medium*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [Longest Palindromic Substring](longest-palindromic-substring.md)

  * [Longest Palindromic Subsequence](longest-palindromic-subsequence.md)

  * [Palindromic Substrings](palindromic-substrings.md)

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
        int sum = 0;
        for (int i = 0; i < s.length(); ++i) {
            sum += palindromeNum(s, i, i);
            sum += palindromeNum(s, i, i + 1);
        }
        
        return sum;
    }
    
private:
    int palindromeNum(const string& s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length()) {
            if (s[left] == s[right]) {
                ++count;
                --left;
                ++right;
            } else {
                return count;
            }
        }
        
        return count;
    }
    
};
```
