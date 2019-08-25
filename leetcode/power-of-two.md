# 231. Power of Two

* *Difficulty: Easy*

* *Topics: Math, Bit Manipulation*

* *Similar Questions:*

  * [Number of 1 Bits](number-of-1-bits.md)

  * [Power of Three](power-of-three.md)

  * [Power of Four](power-of-four.md)

## Problem:

<p>Given an integer, write a function to determine if it is a power of two.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 1
<strong>Output:</strong> true 
<strong>Explanation: </strong>2<sup>0</sup>&nbsp;= 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup>&nbsp;= 16</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 218
<strong>Output:</strong> false</pre>

## Solutions:

```c++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && ((n & (n-1)) == 0);
    }
};
```
