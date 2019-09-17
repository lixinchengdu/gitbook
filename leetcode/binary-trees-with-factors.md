# 843. Binary Trees With Factors

* *Difficulty: Medium*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Given an array of unique integers, each integer is strictly greater than 1.</p>

<p>We make a binary tree using these integers&nbsp;and each number may be used for any number of times.</p>

<p>Each non-leaf node&#39;s&nbsp;value should be equal to the product of the values of it&#39;s children.</p>

<p>How many binary trees can we make?&nbsp; Return the answer <strong>modulo 10 ** 9 + 7</strong>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>A = [2, 4]</code>
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [4, 2, 2]</code></pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>A = [2, 4, 5, 10]</code>
<strong>Output:</strong> <code>7</code>
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]</code>.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;=&nbsp;1000</code>.</li>
	<li><code>2 &lt;=&nbsp;A[i]&nbsp;&lt;=&nbsp;10 ^ 9</code>.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& A) {
        sort(A.begin(), A.end());
        map<int, long> dp;
        
        long ret = 0;
        
        for (int i = 0; i < A.size(); ++i) {
            dp[A[i]] = 1;
            for (auto it = dp.begin(); it != dp.end(); ++it) {
                if (A[i] % it->first == 0 && dp.count(A[i]/it->first)) {
                    dp[A[i]] = (dp[A[i]] + it->second * dp[A[i]/it->first]) % MOD;
                }
            }
            ret = (ret + dp[A[i]]) % MOD;
        }
        
        return ret;
    }
    
private:
    int MOD = 1e9 + 7;
    
};
```
