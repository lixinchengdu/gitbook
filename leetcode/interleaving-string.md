# 97. Interleaving String

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

## Problem:

<p>Given <em>s1</em>, <em>s2</em>, <em>s3</em>, find whether <em>s3</em> is formed by the interleaving of <em>s1</em> and <em>s2</em>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;aabcc&quot;, s2 = &quot;dbbca&quot;, <em>s3</em> = &quot;aadbbcbcac&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;aabcc&quot;, s2 = &quot;dbbca&quot;, <em>s3</em> = &quot;aadbbbaccc&quot;
<strong>Output:</strong> false
</pre>

## Solutions:

```c++
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (s3.length() != s1.length() + s2.length())   return false;
        
        int len1 = s1.length();
        int len2 = s2.length();
        
        vector<vector<bool>> dp (len1 + 1, vector<bool>(len2 + 1, false));
        
        dp[0][0] = true;
        for (int i = 1; i <= len1; ++i) {
            dp[i][0] = dp[i-1][0] && (s1[i-1] == s3[i-1]); 
        }
        
        for (int j = 1; j <=len2; ++j) {
            dp[0][j] = dp[0][j-1] && (s2[j-1] == s3[j-1]);
        }
        
        for (int i = 1; i <= len1; ++i) {
            for (int j = 1; j <= len2; ++j) {
                // i, j denotes count
                dp[i][j] = (s3[i+j -1] == s1[i-1] ? dp[i-1][j] : false ) || (s3[i+j - 1] == s2[j-1] ? dp[i][j-1] : false);            
            }
        }
        
        /*
        for (int i = 0; i <= len1; ++i) {
            for (int j = 0; j <=len2; ++j) {
                cout << dp[i][j] << " ";
            }
            cout << endl;
        }
        */
        
        return dp[len1][len2];
    }
};
```
