# 375. Guess Number Higher or Lower II

* *Difficulty: Medium*

* *Topics: Dynamic Programming, Minimax*

* *Similar Questions:*

  * [Flip Game II](flip-game-ii.md)

  * [Guess Number Higher or Lower](guess-number-higher-or-lower.md)

  * [Can I Win](can-i-win.md)

  * [Find K Closest Elements](find-k-closest-elements.md)

## Problem:

<p>We are playing the Guess Game. The game is as follows:</p>

<p>I pick a number from <strong>1</strong> to <strong>n</strong>. You have to guess which number I picked.</p>

<p>Every time you guess wrong, I&#39;ll tell you whether the number I picked is higher or lower.</p>

<p>However, when you guess a particular number x, and you guess wrong, you pay <b>$x</b>. You win the game when you guess the number I picked.</p>

<p><b>Example:</b></p>

<pre>
n = 10, I pick 8.

First round:  You guess 5, I tell you that it&#39;s higher. You pay $5.
Second round: You guess 7, I tell you that it&#39;s higher. You pay $7.
Third round:  You guess 9, I tell you that it&#39;s lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
</pre>

<p>Given a particular <strong>n &ge; 1</strong>, find out how much money you need to have to guarantee a <b>win</b>.</p>
## Solutions:

```c++
class Solution {
public:
    int getMoneyAmount(int n) {
        if (n <= 0)  return 0;
        vector<vector<int>> dp(n + 1, vector<int> (n + 1, 0));
        
        for (int i = 1; i < n; ++i) {
            dp[i][i+1] = i;
        }
        
        for (int l = 3; l <= n; ++l) {
            for (int i = 1; i <= n - l + 1; ++i) {
                dp[i][i + l - 1] = INT_MAX;
                for (int mid = i + 1; mid <= i + l - 2; ++mid) {
                    dp[i][i + l - 1] = min(dp[i][i + l -1], max(dp[i][mid - 1], dp[mid+1][i + l - 1]) + mid);
                }
            }
        }
        
        return dp[1][n];
        
    }
};
```
