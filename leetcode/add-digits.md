# 258. Add Digits

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Happy Number](happy-number.md)

  * [Sum of Digits in the Minimum Number](sum-of-digits-in-the-minimum-number.md)

## Problem:

<p>Given a non-negative integer <code>num</code>, repeatedly add all its digits until the result has only one digit.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <code>38</code>
<strong>Output:</strong> 2 
<strong>Explanation: </strong>The process is like: <code>3 + 8 = 11</code>, <code>1 + 1 = 2</code>. 
&nbsp;            Since <code>2</code> has only one digit, return it.
</pre>

<p><b>Follow up:</b><br />
Could you do it without any loop/recursion in O(1) runtime?</p>
## Solutions:

```c++
class Solution {
public:
    int addDigits(int num) {
        return 1 + (num - 1) % 9;
    }
};
```
