# 518. Coin Change 2

* *Difficulty: Medium*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.</p>

<ul>
</ul>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> amount = 5, coins = [1, 2, 5]
<b>Output:</b> 4
<b>Explanation:</b> there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> amount = 3, coins = [2]
<b>Output:</b> 0
<b>Explanation:</b> the amount of 3 cannot be made up just with coins of 2.
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> amount = 10, coins = [10] 
<b>Output:</b> 1
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<p>You can assume that</p>

<ul>
	<li>0 &lt;= amount &lt;= 5000</li>
	<li>1 &lt;= coin &lt;= 5000</li>
	<li>the number of coins is less than 500</li>
	<li>the answer is guaranteed to fit into signed 32-bit integer</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int n = coins.size();
        if (n == 0) return amount == 0 ? 1 : 0;
        vector<vector<int>> dp(n, vector<int>(amount + 1, 0));
        for (int i = 0; i < n; ++i) {
            dp[i][0] = 1;
        }
        
        for (int i = 0; i < coins.size(); ++i) {
            for (int j = 1; j <= amount; ++j) {
                dp[i][j] = (i - 1 >= 0 ? dp[i-1][j] : 0) + 
                    (j - coins[i] >= 0 ? dp[i][j - coins[i]] : 0);
            }
        }  
        
        return dp[n-1][amount];
    }
};
```
