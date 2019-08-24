# 7. Reverse Integer

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [String to Integer (atoi)](./tests/reverse-integer.md)

  * [Reverse Bits](./tests/reverse-integer.md)

## Problem:

<p>Given a 32-bit signed integer, reverse digits of an integer.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 123
<strong>Output:</strong> 321
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -123
<strong>Output:</strong> -321
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 120
<strong>Output:</strong> 21
</pre>

<p><strong>Note:</strong><br />
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.</p>

## Solutions:

```c++
class Solution {
public:
    int reverse(int x) {
        if (x == (1<<32)) return 0;
        int sign = (x >= 0 ? 1 : -1);
        int absX = sign * x;
        
        int ret = 0;
        while (absX != 0) {
            int digit = absX%10;
            absX /= 10;
            if (((1 << 31) - 1 - digit)/10 < ret) return 0;
            int newret = 10 * ret + digit;
           // if (newret < ret)    return 0;
            ret = newret;
        }
        return sign*ret;
    }
};
```
