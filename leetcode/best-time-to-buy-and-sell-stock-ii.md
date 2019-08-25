# 122. Best Time to Buy and Sell Stock II

* *Difficulty: Easy*

* *Topics: Array, Greedy*

* *Similar Questions:*

  * [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)

  * [Best Time to Buy and Sell Stock III](best-time-to-buy-and-sell-stock-iii.md)

  * [Best Time to Buy and Sell Stock IV](best-time-to-buy-and-sell-stock-iv.md)

  * [Best Time to Buy and Sell Stock with Cooldown](best-time-to-buy-and-sell-stock-with-cooldown.md)

  * [Best Time to Buy and Sell Stock with Transaction Fee](best-time-to-buy-and-sell-stock-with-transaction-fee.md)

## Problem:

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).</p>

<p><strong>Note:</strong> You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
&nbsp;            Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
</pre>

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
        int profit = 0;
        for (int i = 1; i < prices.size(); ++i) {
            profit += max(0, prices[i] - prices[i-1]); 
        }
        return profit;
    }
};
```
