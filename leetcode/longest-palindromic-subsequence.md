# 516. Longest Palindromic Subsequence

* *Difficulty: Medium*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Longest Palindromic Substring](longest-palindromic-substring.md)

  * [Palindromic Substrings](palindromic-substrings.md)

  * [Count Different Palindromic Subsequences](count-different-palindromic-subsequences.md)

  * [Longest Common Subsequence](longest-common-subsequence.md)

## Problem:

<p>
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
</p>

<p><b>Example 1:</b><br>
Input: 
<pre>
"bbbab"
</pre>
Output: 
<pre>
4
</pre>
One possible longest palindromic subsequence is "bbbb".
</p>

<p><b>Example 2:</b><br>
Input:
<pre>
"cbbd"
</pre>
Output:
<pre>
2
</pre>
One possible longest palindromic subsequence is "bb".
</p>
## Solutions:

```c++
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.length();
        if (n == 0) return 0;
        vector<vector<int>> dp (n, vector<int>(n, 0));
        
        for (int i = 0; i < s.length(); ++i) {
            dp[i][i] = 1;
        }
        
        for (int l = 2; l <= s.length(); ++l) {
            for (int i = 0; i < s.length(); ++i) {
                int left = i;
                int right = i + l - 1;
                if (right >= n) break;
                dp[left][right] = max(dp[left][right-1], dp[left+1][right]);
                if (s[left] == s[right]) {
                    dp[left][right] = max(dp[left][right], 2 + dp[left + 1][right - 1]);
                }
            }
        }
        
        return dp[0][n-1];
    }
};
```
