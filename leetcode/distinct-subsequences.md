# 115. Distinct Subsequences

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

## Problem:

<p>Given a string <strong>S</strong> and a string <strong>T</strong>, count the number of distinct subsequences of <strong>S</strong> which equals <strong>T</strong>.</p>

<p>A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, <code>&quot;ACE&quot;</code> is a subsequence of <code>&quot;ABCDE&quot;</code> while <code>&quot;AEC&quot;</code> is not).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <code>&quot;rabbbit&quot;</code>, T = <code>&quot;rabbit&quot;
<strong>Output:</strong>&nbsp;3
</code><strong>Explanation:
</strong>
As shown below, there are 3 ways you can generate &quot;rabbit&quot; from S.
(The caret symbol ^ means the chosen letters)

<code>rabbbit</code>
^^^^ ^^
<code>rabbbit</code>
^^ ^^^^
<code>rabbbit</code>
^^^ ^^^
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <code>&quot;babgbag&quot;</code>, T = <code>&quot;bag&quot;
<strong>Output:</strong>&nbsp;5
</code><strong>Explanation:
</strong>
As shown below, there are 5 ways you can generate &quot;bag&quot; from S.
(The caret symbol ^ means the chosen letters)

<code>babgbag</code>
^^ ^
<code>babgbag</code>
^^    ^
<code>babgbag</code>
^    ^^
<code>babgbag</code>
  ^  ^^
<code>babgbag</code>
    ^^^
</pre>

## Solutions:

```c++
class Solution {
public:
    int numDistinct(string s, string t) {
        int sLen = s.length();
        int tLen = t.length();
        
        vector<vector<long>> dp(sLen + 1, vector<long> (tLen + 1, 0));
        dp[0][0] = 1;
        
        for (int i = 1; i <= sLen; ++i) {
            dp[i][0] = 1;
        }
        
        for (int j = 1; j <= tLen; ++j) {
            dp[0][j] = 0;
        }
        
        for (int i = 1; i <= sLen; ++i) {
            for (int j = 1; j <=tLen; ++j) {
                dp[i][j] = dp[i-1][j];
                if (s[i-1] == t[j-1]) {
                    dp[i][j] += dp[i-1][j-1];
                }
            }
        }
        return dp[sLen][tLen];
    }
};
```
