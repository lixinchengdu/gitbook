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
        int low = 0;
        int high = (int) sqrt(2*(long)n) + 1;
        //long longN = 2*(long)n;
        //cout << sqrt(longN) << endl;
        //cout << "low:" << low << " high:" << high << endl;
        while (low + 1 < high)
        {
            //cout << "low:" << low << " high:" << high << endl;
            int mid = low + (high-low)/2;
            if (mid == 60071)
            {
                ;
                //cout << "left:" << fullNumber(mid) << " right:" << n << endl;
            }
            if (fullNumber(mid) == n)    return mid;
            else if (fullNumber(mid) > n )   high = mid;
            else low = mid;
        }
        cout << low << " " << high << endl;
        if (fullNumber(high) != n)  return low;
        else    return high;
        
    }
    long fullNumber (int level)
    {
        long l_level = (long) level;
        return l_level*(l_level+1)/2;
    }
};
```
