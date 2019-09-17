# 309. Best Time to Buy and Sell Stock with Cooldown

* *Difficulty: Medium*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)

  * [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii.md)

## Problem:

<p>Say you have an array for which the <i>i</i><sup>th</sup> element is the price of a given stock on day <i>i</i>.</p>

<p>Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:</p>

<ul>
	<li>You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).</li>
	<li>After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)</li>
</ul>

<p><b>Example:</b></p>

<pre>
<strong>Input:</strong> [1,2,3,0,2]
<strong>Output: </strong>3 
<strong>Explanation:</strong> transactions = [buy, sell, cooldown, buy, sell]
</pre>
## Solutions:

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;
        vector<int> sell(n, 0);
        vector<int> hold(n, 0);
        
        for (int i = 0; i < n; ++i) {
            hold[i] = max(i - 1 >= 0 ? hold[i-1] : INT_MIN, i - 2 >= 0 ? -prices[i] + sell[i-2] : -prices[i]);
            sell[i] = (i - 1 >= 0 ? max(hold[i-1] + prices[i], sell[i-1]) : 0);
        }
        
        return sell[n-1];
    }
};
```
