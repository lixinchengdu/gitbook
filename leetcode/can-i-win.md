# 464. Can I Win

* *Difficulty: Medium*

* *Topics: Dynamic Programming, Minimax*

* *Similar Questions:*

  * [Flip Game II](flip-game-ii.md)

  * [Guess Number Higher or Lower II](guess-number-higher-or-lower-ii.md)

  * [Predict the Winner](predict-the-winner.md)

## Problem:

<p>In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins. </p>

<p>What if we change the game so that players cannot re-use integers? </p>

<p>For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.</p>

<p>Given an integer <code>maxChoosableInteger</code> and another integer <code>desiredTotal</code>, determine if the first player to move can force a win, assuming both players play optimally. </p>

<p>You can always assume that <code>maxChoosableInteger</code> will not be larger than 20 and <code>desiredTotal</code> will not be larger than 300.
</p>

<p><b>Example</b>
<pre>
<b>Input:</b>
maxChoosableInteger = 10
desiredTotal = 11

<b>Output:</b>
false

<b>Explanation:</b>
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desireTotal) {
        int pool = 0;
        for (int i = 1; i <= maxChoosableInteger; ++i) {
            pool = pool | (1 << i);
        }
        if ((maxChoosableInteger + 1) * maxChoosableInteger / 2 < desireTotal)  return false;
        map<pair<int, int>, bool> cache;
        
        return helper(pool, desireTotal, maxChoosableInteger, cache);
    }
private:
    bool helper(int pool, int desireTotal, int maxChoosableInteger, map<pair<int, int>, bool>& cache) {
        if (cache.count({pool, desireTotal}) > 0)   return cache[{pool, desireTotal}];
        
        bool ret = false;
        for (int i = 1; i <= maxChoosableInteger; ++i) {
            if ((pool >> i) & (0x1)) {
                int newPool = pool & (~(1 << i));
                if (desireTotal - i <= 0) {
                    ret = true;
                    break;
                }
                bool enemy = helper(newPool, desireTotal - i, maxChoosableInteger, cache);
                if (!enemy) {
                    ret = true;
                    break;
                }
            }
        }
        cache[{pool, desireTotal}] = ret;
        return ret;
        
    }
    
};
```
