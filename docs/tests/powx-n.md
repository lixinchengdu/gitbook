# 50. Pow(x, n)

* *Difficulty: Medium*

* *Topics: Math, Binary Search*

* *Similar Questions:*

  * [Sqrt(x)](./tests/powx-n.md)

  * [Super Pow](./tests/powx-n.md)

## Problem:

<p>Implement <a href="http://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(<em>x</em>, <em>n</em>)</a>, which calculates&nbsp;<em>x</em> raised to the power <em>n</em> (x<sup><span style="font-size:10.8333px">n</span></sup>).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 2.00000, 10
<strong>Output:</strong> 1024.00000
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 2.10000, 3
<strong>Output:</strong> 9.26100
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 2.00000, -2
<strong>Output:</strong> 0.25000
<strong>Explanation:</strong> 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>-100.0 &lt; <em>x</em> &lt; 100.0</li>
	<li><em>n</em> is a 32-bit signed integer, within the range&nbsp;[&minus;2<sup>31</sup>,&nbsp;2<sup>31&nbsp;</sup>&minus; 1]</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    double myPow(double x, int n) {
        int sign = (n >= 0? 1 : -1);
        bool overflow = false;
        if (n == INT_MIN) {
            overflow = true;
            n = INT_MIN + 1;
        }
        n = abs(n);
        
        double origin_x = x;
        double ret = 1;
        while (n > 0) {
            if (n&1) {
                ret *= x;
            }
            n = (n >> 1);
            x = x * x;
        }
        if (overflow)   ret *= origin_x;
        return sign == 1 ? ret : 1/ret;
    }
};
```
