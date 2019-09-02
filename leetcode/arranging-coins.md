# 441. Arranging Coins

* *Difficulty: Easy*

* *Topics: Math, Binary Search*

* *Similar Questions:*

## Problem:

<p>You have a total of <i>n</i> coins that you want to form in a staircase shape, where every <i>k</i>-th row must have exactly <i>k</i> coins.</p>
 
<p>Given <i>n</i>, find the total number of <b>full</b> staircase rows that can be formed.</p>

<p><i>n</i> is a non-negative integer and fits within the range of a 32-bit signed integer.</p>

<p><b>Example 1:</b>
<pre>
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
</pre>
</p>

<p><b>Example 2:</b>
<pre>
n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    int arrangeCoins(int n) {
        long left = 0;
        long right = INT_MAX / 4;
        
        while (left < right) {
            long mid = right - (right - left) / 2;
            if ( (mid + 1) * mid / 2 > n)  {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        
        return left;
    }
};
```
