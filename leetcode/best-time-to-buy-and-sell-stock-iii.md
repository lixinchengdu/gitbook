# 123. Best Time to Buy and Sell Stock III

* *Difficulty: Hard*

* *Topics: Array, Dynamic Programming*

* *Similar Questions:*

  * [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)

  * [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii.md)

  * [Best Time to Buy and Sell Stock IV](best-time-to-buy-and-sell-stock-iv.md)

  * [Maximum Sum of 3 Non-Overlapping Subarrays](maximum-sum-of-3-non-overlapping-subarrays.md)

## Problem:

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>Design an algorithm to find the maximum profit. You may complete at most <em>two</em> transactions.</p>

<p><strong>Note:&nbsp;</strong>You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,3,5,0,0,3,1,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
&nbsp;            Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
&nbsp;            Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
&nbsp;            engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.</pre>

## Solutions:

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;
        
        vector<int> forward(n, 0);
        vector<int> backward(n, 0);
        
        int minVal = prices[0];
        for (int i = 1; i < n; ++i) {
            forward[i] = max(forward[i - 1], prices[i] - minVal);
            minVal = min(minVal, prices[i]);
        }
        
        int maxVal = prices[n-1];
        for (int i = n - 2; i >= 0; --i) {
            backward[i] = max(backward[i + 1], maxVal - prices[i]);
            maxVal = max(maxVal, prices[i]);
        }
        
        int ret = 0;
        for (int i = 0; i < n; ++i) {
            ret = max(ret, forward[i] + backward[i]);
        }
        
        return ret;
    }
};
```
