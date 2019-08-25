# 132. Palindrome Partitioning II

* *Difficulty: Hard*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Palindrome Partitioning](palindrome-partitioning.md)

## Problem:

<p>Given a string <em>s</em>, partition <em>s</em> such that every substring of the partition is a palindrome.</p>

<p>Return the minimum cuts needed for a palindrome partitioning of <em>s</em>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;&quot;aab&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The palindrome partitioning [&quot;aa&quot;,&quot;b&quot;] could be produced using 1 cut.
</pre>

## Solutions:

```c++
class Solution {
public:
    int minCut(string s) {
        int len = s.length();
        vector<vector<bool>> dp(len, vector<bool>(len, false));
        for (int j = 0; j < len; ++j) {
            for (int i = 0; i <= j; ++i) {
                if (s[i] == s[j] && (j - i <= 2 || dp[i+1][j-1])) {
                    dp[i][j] = true;
                }
            }
        }
        
        vector<int> cache (len, INT_MAX);
        return helper(s, 0, dp, cache) - 1;
    }
    
    int helper(string& s, int start, vector<vector<bool>>& dp, vector<int>& cache) {
        if (start >= s.length())    return 0;
        if (cache[start] != INT_MAX)    return cache[start];
        int ret = INT_MAX;
        for (int i = start; i < s.length(); ++i) {
            if (dp[start][i]) {
                ret = min(ret, 1 + helper(s, i + 1, dp, cache)); 
            }
        }
        
        cache[start] = ret;                  
        return ret;
    }
};
```
