# 69. Sqrt(x)

* *Difficulty: Easy*

* *Topics: Math, Binary Search*

* *Similar Questions:*

  * [Pow(x, n)](./tests/sqrtx.md)

  * [Valid Perfect Square](./tests/sqrtx.md)

## Problem:

<p>Implement <code>int sqrt(int x)</code>.</p>

<p>Compute and return the square root of <em>x</em>, where&nbsp;<em>x</em>&nbsp;is guaranteed to be a non-negative integer.</p>

<p>Since the return type&nbsp;is an integer, the decimal digits are truncated and only the integer part of the result&nbsp;is returned.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 4
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.82842..., and since 
&nbsp;            the decimal part is truncated, 2 is returned.
</pre>

## Solutions:

```c++
class Solution {
public:
    int sqrt(int x) {
        unsigned long long start=0;
        unsigned long long end=x;
        unsigned long long pivot=(start+end)/2;
        while (pivot*pivot!=x ||start!=end)
        {
            if(pivot*pivot>x)
            {
                end=pivot-1;
                pivot=(start+end)/2;
            }
            else
            {   if (start==pivot)
            {
                return end*end<=x? end:pivot;
            }
                start=pivot;
                pivot=(start+end)/2;
            }
        }
        return pivot;
        
    }
};
```
