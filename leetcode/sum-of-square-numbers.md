# 633. Sum of Square Numbers

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Valid Perfect Square](valid-perfect-square.md)

## Problem:

<p>Given a non-negative integer <code>c</code>, your task is to decide whether there&#39;re two integers <code>a</code> and <code>b</code> such that a<sup>2</sup> + b<sup>2</sup> = c.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 5
<b>Output:</b> True
<b>Explanation:</b> 1 * 1 + 2 * 2 = 5
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 3
<b>Output:</b> False
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    bool judgeSquareSum(int c) {
        long left = 0;
        long right = sqrt(c) + 1;
        
        while (left <= right) {
            long sum = left * left + right * right;
            if (sum == c)   return true;
            else if (sum > c) {
                --right;
            } else {
                ++left;
            }
        }
        
        return false;
    }
};
```
