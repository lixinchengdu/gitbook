# 121. Best Time to Buy and Sell Stock

* *Difficulty: Easy*

* *Topics: Array, Dynamic Programming*

* *Similar Questions:*

  * [Maximum Subarray](maximum-subarray.md)

  * [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii.md)

  * [Best Time to Buy and Sell Stock III](best-time-to-buy-and-sell-stock-iii.md)

  * [Best Time to Buy and Sell Stock IV](best-time-to-buy-and-sell-stock-iv.md)

  * [Best Time to Buy and Sell Stock with Cooldown](best-time-to-buy-and-sell-stock-with-cooldown.md)

## Problem:

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.</p>

<p>Note that you cannot sell a stock before you buy one.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
&nbsp;            Not 7-1 = 6, as selling price needs to be larger than buying price.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.
</pre>

## Solutions:

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = INT_MAX;
        int profit = 0;
        for (auto price : prices) {
            buy = min(buy, price);
            profit = max(profit, price - buy);
        }
        
        return profit;
    }
};
```
