# 69. Sqrt(x)

* *Difficulty: Easy*

* *Topics: Math, Binary Search*

* *Similar Questions:*

  * [Pow(x, n)](powx-n.md)

  * [Valid Perfect Square](valid-perfect-square.md)

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
    int mySqrt(int x) {
        int left = 0;
        int right = INT_MAX;
        while (left + 1 < right) {
            int mid = left + (right - left)/2;
            if (x/mid >= mid) { // mid * mid <= x would cause overflow
                left = mid;
            } else {
                right = mid;
            }
        }
        
        if (x/right >= right)   return right;
        return left;
    }
};
```
