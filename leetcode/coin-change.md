# 322. Coin Change

* *Difficulty: Medium*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Minimum Cost For Tickets](minimum-cost-for-tickets.md)

## Problem:

<p>You are given coins of different denominations and a total amount of money <i>amount</i>. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input: </strong>coins = <code>[1, 2, 5]</code>, amount = <code>11</code>
<strong>Output: </strong><code>3</code> 
<strong>Explanation:</strong> 11 = 5 + 5 + 1</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input: </strong>coins = <code>[2]</code>, amount = <code>3</code>
<strong>Output: </strong>-1
</pre>

<p><b>Note</b>:<br />
You may assume that you have an infinite number of each kind of coin.</p>

## Solutions:

```c++
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount < 0) return -1;
        if (amount == 0) return 0; // retrun 0
        
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i < coins.size(); ++i) {
            int val = coins[i];
            for (int j = 0; j <= amount; ++j) {
                // transition function
                dp[j] = min(dp[j], j - val >= 0 && dp[j - val] != INT_MAX ? 1 + dp[j - val] : INT_MAX); // check INT_MAX
            }
        }
        
        return dp[amount] == INT_MAX ? -1 : dp[amount]; // check INT_MAX
    }
};
```
