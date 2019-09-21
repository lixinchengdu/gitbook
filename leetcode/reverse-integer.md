# 7. Reverse Integer

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [String to Integer (atoi)](string-to-integer-atoi.md)

  * [Reverse Bits](reverse-bits.md)

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
        bool sign = (x >= 0);
        if (x == INT_MIN)   return 0;
        x = abs(x); // it is wrong if x is INT_MIN because of overflow.
        
        int ret = 0;
        while (x > 0) {
            int digit = x%10;
            x /= 10;
            if (ret > INT_MAX/10 || (ret == INT_MAX/10 && (sign ? digit > INT_MAX%10 : digit > INT_MAX%10 + 1)))    return 0; // the priority of conditional operator is low && abs(INT_MIN) is forbidon!!!
            ret = ret * 10 + digit;
        }
        
        return sign ? ret : -ret;
    }
};
```

### More concise solution

From [https://zxi.mytechroad.com/blog/simulation/leetcode-7-reverse-integer/](Huahua)

It is not necessary to distinguish whether `x` is negative or not. 

The rule to determine the sign of modulus is explained at one [https://stackoverflow.com/questions/7594508/modulo-operator-with-negative-values](article from StackOverFlow).  
Simple examples are shown below. 

<pre>
(-7/3) => -2
-2 * 3 => -6
so a%b => -1

(7/-3) => -2
-2 * -3 => 6
so a%b => 1
</pre>

```c++
// Author: Huahua
class Solution {
public:
  int reverse(int x) {
    int ans = 0;
    while (x != 0) {
      int r = x % 10;
      if (ans > INT_MAX / 10 || ans < INT_MIN / 10) return 0;
      ans = ans * 10 + r;
      x /= 10;
    }
    return ans;
  }
};
```
