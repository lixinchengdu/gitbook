# 367. Valid Perfect Square

* *Difficulty: Easy*

* *Topics: Math, Binary Search*

* *Similar Questions:*

  * [Sqrt(x)](sqrtx.md)

  * [Sum of Square Numbers](sum-of-square-numbers.md)

## Problem:

<p>Given a positive integer <i>num</i>, write a function which returns True if <i>num</i> is a perfect square else False.</p>

<p><b>Note:</b> <b>Do not</b> use any built-in library function such as <code>sqrt</code>.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">16</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">14</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    bool isPerfectSquare(int num) {
        int left = 1; // left is 1!
        int right = INT_MAX;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (num / mid > mid) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return num % left == 0 && num / left == left;
    }
};
```
