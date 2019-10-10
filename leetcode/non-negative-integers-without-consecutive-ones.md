# 600. Non-negative Integers without Consecutive Ones

* *Difficulty: Hard*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [House Robber](house-robber.md)

  * [House Robber II](house-robber-ii.md)

  * [Ones and Zeroes](ones-and-zeroes.md)

## Problem:

<p>Given a positive integer n, find the number of <b>non-negative</b> integers less than or equal to n, whose binary representations do NOT contain <b>consecutive ones</b>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 5
<b>Output:</b> 5
<b>Explanation:</b> 
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
</pre>
</p>

<p><b>Note:</b>
1 <= n <= 10<sup>9</sup>
</p>

## Solutions:

```c++
class Solution {
public:
    int findIntegers(int num) {
        unordered_map<int, int> cache;
        return helper(num, 31, cache);
    }
    
private:
    int helper(int num, int pos, unordered_map<int, int>& cache) {
        // cout << num << " " << pos << endl;
        if (cache.count(num))   return cache[num];
        if (pos < 0)  return 1;
        if ((num & (1 << pos)) == 0) {
            return helper(num, pos - 1, cache);
        }    
        
        if (pos == 0) {
            return 2;
        }
        
        if (pos == 1) {
            return 3;
        }
        
        int ret;
        int num1 = (1 << pos) - 1;
        int num2 = 
            ((num & (1 << (pos - 1))) == 0) ? num & (~(3 << (pos - 1))) : (1 << (pos - 1)) - 1;
        ret = helper(num1, pos - 1, cache) + helper(num2, pos - 2, cache);
        
        cache[num] = ret;
        return ret;
    }
    
};
```
