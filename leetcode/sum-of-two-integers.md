# 371. Sum of Two Integers

* *Difficulty: Easy*

* *Topics: Bit Manipulation*

* *Similar Questions:*

  * [Add Two Numbers](add-two-numbers.md)

## Problem:

<p>Calculate the sum of two integers <i>a</i> and <i>b</i>, but you are <b>not allowed</b> to use the operator <code>+</code> and <code>-</code>.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>a = <span id="example-input-1-1">1</span>, b = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">3</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>a = -<span id="example-input-2-1">2</span>, b = <span id="example-input-2-2">3</span>
<strong>Output: </strong>1
</pre>
</div>
</div>

## Solutions:

```c++
class Solution {
public:
    int getSum(int a, int b) {
        int ret = a^b;
        int carry = a&b;
        
        while (carry != 0) {
            // to prevent runtime exception, &0x7fffffff; This is not necessary for real program. Platforms other than leetcode do not complain. 
            carry = (carry & 0x7fffffff)<< 1; 
            int newRet = ret^carry;
            int newCarry = ret&carry;
            ret = newRet;
            carry = newCarry;
        }
        
        return ret;
    }
};
```
