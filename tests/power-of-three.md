# 326. Power of Three

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Power of Two](./tests/power-of-three.md)

  * [Power of Four](./tests/power-of-three.md)

## Problem:

<p>Given an integer, write a function to determine if it is a power of three.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input:</strong> 27
<strong>Output:</strong> true
</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input:</strong> 0
<strong>Output:</strong> false</pre>

<p><b>Example 3:</b></p>

<pre>
<strong>Input:</strong> 9
<strong>Output:</strong> true</pre>

<p><b>Example 4:</b></p>

<pre>
<strong>Input:</strong> 45
<strong>Output:</strong> false</pre>

<p><b>Follow up:</b><br />
Could you do it without using any loop / recursion?</p>
## Solutions:

```c++
class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n == 0) return false;
        if (n == 1) return true;
        return n%3 == 0 ? isPowerOfThree(n/3) : false;
    }
};
```
