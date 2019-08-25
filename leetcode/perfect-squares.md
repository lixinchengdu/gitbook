# 279. Perfect Squares

* *Difficulty: Medium*

* *Topics: Math, Dynamic Programming, Breadth-first Search*

* *Similar Questions:*

  * [Count Primes](count-primes.md)

  * [Ugly Number II](ugly-number-ii.md)

## Problem:

<p>Given a positive integer <i>n</i>, find the least number of perfect square numbers (for example, <code>1, 4, 9, 16, ...</code>) which sum to <i>n</i>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <i>n</i> = <code>12</code>
<b>Output:</b> 3 
<strong>Explanation: </strong><code>12 = 4 + 4 + 4.</code></pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <i>n</i> = <code>13</code>
<b>Output:</b> 2
<strong>Explanation: </strong><code>13 = 4 + 9.</code></pre>
## Solutions:

```c++
class Solution {
public:
    int numSquares(int n) {
        queue<int> q;
        unordered_set<int> visited;
        
        q.push(n);
        visited.insert(n);
        int level = 0;
        while(true) {
            ++level;
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                int sum = q.front(); q.pop();
                for (int sqrt = 1; sqrt <= sum/sqrt; ++sqrt) {
                    if (sum == sqrt * sqrt) return level;
                    int remaining = sum - sqrt * sqrt;
                    if (visited.count(remaining) > 0)   continue;
                    visited.insert(remaining);
                    q.push(remaining);
                }
            }
        }
        
        return -1;
    }
};
```
