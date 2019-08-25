# 188. Best Time to Buy and Sell Stock IV

* *Difficulty: Hard*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md)

  * [Best Time to Buy and Sell Stock II](best-time-to-buy-and-sell-stock-ii.md)

  * [Best Time to Buy and Sell Stock III](best-time-to-buy-and-sell-stock-iii.md)

## Problem:

<p>Say you have an array for which the <i>i<span style="font-size: 10.8333px;">-</span></i><span style="font-size: 10.8333px;">th</span>&nbsp;element is the price of a given stock on day <i>i</i>.</p>

<p>Design an algorithm to find the maximum profit. You may complete at most <b>k</b> transactions.</p>

<p><b>Note:</b><br />
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,4,1], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [3,2,6,5,0,3], k = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
&nbsp;            Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
</pre>

## Solutions:

```c++
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if (k == 0 || n == 0) return 0;
        
        k = min(k, n/2);
        
        vector<vector<int>> hold (n , vector<int> (2, 0));
        vector<vector<int>> empty(n , vector<int> (2, 0));
        
        for (int i = 0; i < n; ++i) {
            empty[i][0] = 0;
        }
        
        for (int j = 1; j <= k; ++j) {
            hold[0][j%2] = -prices[0];
            empty[0][j%2] = 0;
        }
        
        
        for (int j = 1; j <= k; ++j) {
            for (int i = 1; i < n; ++i) {
                hold[i][j%2] = max(hold[i-1][j%2], empty[i-1][(j-1)%2] - prices[i]);
                empty[i][j%2] = max(empty[i-1][j%2], hold[i-1][j%2] + prices[i]);        
            }
        }  
        
        return empty[n-1][k%2];
    }
};
```
