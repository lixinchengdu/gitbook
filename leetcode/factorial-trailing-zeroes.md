# 172. Factorial Trailing Zeroes

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Number of Digit One](number-of-digit-one.md)

  * [Preimage Size of Factorial Zeroes Function](preimage-size-of-factorial-zeroes-function.md)

## Problem:

<p>Given an integer <i>n</i>, return the number of trailing zeroes in <i>n</i>!.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;3! = 6, no trailing zero.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 5
<strong>Output:</strong> 1
<strong>Explanation:</strong>&nbsp;5! = 120, one trailing zero.</pre>

<p><b>Note: </b>Your solution should be in logarithmic time complexity.</p>

## Solutions:

```c++
class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        int divisor = 5;
        while (n >= divisor) {
            count += n/divisor;
            n /= 5; // be careful about overflow!
        } 
        
        return count;
    }
};
```
