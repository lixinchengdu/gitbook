# 70. Climbing Stairs

* *Difficulty: Easy*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Min Cost Climbing Stairs](./tests/climbing-stairs.md)

  * [Fibonacci Number](./tests/climbing-stairs.md)

  * [N-th Tribonacci Number](./tests/climbing-stairs.md)

## Problem:

<p>You are climbing a stair case. It takes <em>n</em> steps to reach to the top.</p>

<p>Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?</p>

<p><strong>Note:</strong> Given <em>n</em> will be a positive integer.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

## Solutions:

```c++
class Solution {
public:
    int climbStairs(int n) {
        int a= 1, b = 1;
        int a_next, b_next;
        for (int i =2; i <= n; i++)
        {
            a_next = a + b;
            b_next = a; 
            
            a = a_next;
            b = b_next;
        }
        
        return a;
        
    }
};
```
