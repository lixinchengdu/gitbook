# 221. Maximal Square

* *Difficulty: Medium*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Maximal Rectangle](maximal-rectangle.md)

  * [Largest Plus Sign](largest-plus-sign.md)

## Problem:

<p>Given a 2D binary matrix filled with 0&#39;s and 1&#39;s, find the largest square containing only 1&#39;s and return its area.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: 
</strong>
1 0 1 0 0
1 0 <font color="red">1</font> <font color="red">1</font> 1
1 1 <font color="red">1</font> <font color="red">1</font> 1
1 0 0 1 0

<strong>Output: </strong>4
</pre>
## Solutions:

```c++
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        if (m == 0) return 0;
        int n = matrix[0].size();
        if (n == 0) return 0;
        
        vector<vector<int>> dp(m, vector<int> (n, 0));
        
        for (int i = 0; i < m; ++i) {
            dp[i][0] = matrix[i][0] - '0';
        }
        
        for (int j = 0; j < n; ++j) {
            dp[0][j] = matrix[0][j] - '0';
        }
        
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][j] != '0') {
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]));
                }
            }
        }
        
        int ret = 0;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ret = max(ret, dp[i][j]);
            }
        }
        
        return ret * ret;
    }
};
```
