# 342. Power of Four

* *Difficulty: Easy*

* *Topics: Bit Manipulation*

* *Similar Questions:*

  * [Power of Two](power-of-two.md)

  * [Power of Three](power-of-three.md)

## Problem:

<p>Given an integer (signed 32 bits), write a function to check whether it is a power of 4.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">16</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">5</span>
<strong>Output: </strong><span id="example-output-2">false</span></pre>
</div>

<p><b>Follow up</b>: Could you solve it without loops/recursion?</p>
## Solutions:

```c++
class Solution {
public:
    bool isPowerOfFour(int num) {
        return num > 0 && ((num & (num - 1)) == 0) && ((num & 0x55555555) != 0);
    }
};
```
