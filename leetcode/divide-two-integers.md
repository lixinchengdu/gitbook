# 29. Divide Two Integers

* *Difficulty: Medium*

* *Topics: Math, Binary Search*

* *Similar Questions:*

## Problem:

<p>Given two integers <code>dividend</code> and <code>divisor</code>, divide two integers without using multiplication, division and mod operator.</p>

<p>Return the quotient after dividing <code>dividend</code> by <code>divisor</code>.</p>

<p>The integer division should truncate toward zero.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> dividend = 10, divisor = 3
<strong>Output:</strong> 3</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> dividend = 7, divisor = -3
<strong>Output:</strong> -2</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>Both dividend and divisor&nbsp;will be&nbsp;32-bit&nbsp;signed integers.</li>
	<li>The divisor will never be 0.</li>
	<li>Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;2<sup>31</sup>, &nbsp;2<sup>31</sup> &minus; 1]. For the purpose of this problem, assume that your function returns 2<sup>31</sup> &minus; 1 when the division result&nbsp;overflows.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1)   return INT_MAX;
        if (dividend == INT_MIN && divisor == 1)    return INT_MIN;
        if (dividend == INT_MIN && divisor == INT_MIN)  return 1;
        if (divisor == INT_MIN) {
            return 0;
        }
        
        int sign = 1;
        if ((dividend >= 0 && divisor < 0) || (dividend < 0 && divisor >= 0)) {
            sign = -1;
        }
        divisor = abs(divisor);
        int carry = 0;
        if (dividend == INT_MIN) {
            dividend += divisor;
            carry = 1;
        }
        dividend = abs(dividend);
        
        
        int ret = 0;
        while (dividend >= divisor) {
            int q = 1;
            int d = divisor;
            int half = dividend >> 1;
            while (half >= d) {
                d <<= 1;
                q <<= 1;
            }
            
            ret += q;
            dividend -= d;
        }
        ret += carry; // add carry because it is negative
        return ret * sign;
    }
};
```
