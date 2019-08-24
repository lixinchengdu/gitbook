# 44. Wildcard Matching

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming, Backtracking, Greedy*

* *Similar Questions:*

  * [Regular Expression Matching](./tests/wildcard-matching.md)

## Problem:

<p>Given an input string (<code>s</code>) and a pattern (<code>p</code>), implement wildcard pattern matching with support for <code>&#39;?&#39;</code> and <code>&#39;*&#39;</code>.</p>

<pre>
&#39;?&#39; Matches any single character.
&#39;*&#39; Matches any sequence of characters (including the empty sequence).
</pre>

<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>s</code>&nbsp;could be empty and contains only lowercase letters <code>a-z</code>.</li>
	<li><code>p</code> could be empty and contains only lowercase letters <code>a-z</code>, and characters like <code><font face="monospace">?</font></code>&nbsp;or&nbsp;<code>*</code>.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aa&quot;
p = &quot;a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;a&quot; does not match the entire string &quot;aa&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aa&quot;
p = &quot;*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&#39;*&#39; matches any sequence.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;cb&quot;
p = &quot;?a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong>&nbsp;&#39;?&#39; matches &#39;c&#39;, but the second letter is &#39;a&#39;, which does not match &#39;b&#39;.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;adceb&quot;
p = &quot;*a*b&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;The first &#39;*&#39; matches the empty sequence, while the second &#39;*&#39; matches the substring &quot;dce&quot;.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;acdcb&quot;
p = &quot;a*c?b&quot;
<strong>Output:</strong> false
</pre>

## Solutions:

```c++
class Solution {
public:
    bool isMatch(string s, string p) {
        int n1 = s.size();
        int n2 = p.size();
        if (n1 == 0 && n2 == 0) return true;
        vector <vector<bool>> dp (n1 + 1, vector<bool>(n2 + 1, false));
        dp[0][0] = true;
    
        for (int i = 0; i < n1 + 1; i++)
        {
            for (int j = 0; j < n2 + 1; j++)
            {
                if (i == 0 && j == 0)   continue;
                if (i > 0 && j > 0 && (s[i-1] == p[j-1] || p[j-1] == '?'))    dp[i][j] = dp[i-1][j-1];
                else if (j > 0 && p[j-1] == '*')   dp[i][j] =  dp[i][j-1] || (i > 0? dp[i-1][j]: false);
                else    dp[i][j] = false;
            }
        }
        return dp[n1][n2];
    }
};
```
