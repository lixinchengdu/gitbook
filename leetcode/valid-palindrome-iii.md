# 1178. Valid Palindrome III

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

## Problem:

<p>Given a string <code>s</code>&nbsp;and an integer&nbsp;<code>k</code>, find out if the given string is&nbsp;a&nbsp;<em>K-Palindrome</em> or not.</p>

<p>A string is K-Palindrome if it can be&nbsp;transformed&nbsp;into a palindrome by removing at most <code>k</code> characters from it.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcdeca&quot;, k = 2
<strong>Output:</strong> true
<strong>Explanation: </strong>Remove &#39;b&#39; and &#39;e&#39; characters.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code>&nbsp;has only lowercase English letters.</li>
	<li><code>1 &lt;= k&nbsp;&lt;= s.length</code></li>
</ul>

## Solutions:

```c++
class Solution {
public:
    bool isValidPalindrome(string s, int k) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i <= n - len; ++i) {
                int left = i;
                int right = i + len - 1;
                dp[left][right] = 1 + min(dp[left + 1][right], dp[left][right - 1]);
                if (s[left] == s[right]) {
                    dp[left][right] = min(dp[left][right], dp[left+1][right-1]);
                }
            }
        }
        
        return dp[0][n-1] <= k;
    }
};
```
