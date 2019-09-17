# 365. Water and Jug Problem

* *Difficulty: Medium*

* *Topics: Math*

* *Similar Questions:*

## Problem:

<p>You are given two jugs with capacities <i>x</i> and <i>y</i> litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly <i>z</i> litres using these two jugs.</p>

<p>If <i>z</i> liters of water is measurable, you must have <i>z</i> liters of water contained within <b>one or both buckets</b> by the end.</p>

<p>Operations allowed:</p>

<ul>
	<li>Fill any of the jugs completely with water.</li>
	<li>Empty any of the jugs.</li>
	<li>Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.</li>
</ul>

<p><b>Example 1:</b> (From the famous <a href="https://www.youtube.com/watch?v=BVtQNK_ZUJg" target="_blank"><i>&quot;Die Hard&quot;</i> example</a>)</p>

<pre>
Input: x = 3, y = 5, z = 4
Output: True
</pre>

<p><b>Example 2:</b></p>

<pre>
Input: x = 2, y = 6, z = 5
Output: False
</pre>
## Solutions:

```c++
class Solution {
public:
    bool canMeasureWater(int x, int y, int z) {
        // ax + by = z
        if (z ==0)  return true;
        if (x + y < z) return false;
        if (x != 0 && y != 0) {
            int divisor = gcd(x, y);
            return z % divisor == 0;
        } else return false;
    }
    
private:
    int gcd (int x, int y) {
        if (y > x) {
            return gcd(y, x);
        }
        
        if (y == 0) return x;
        return gcd(y, x % y);
    }
    
};
```
