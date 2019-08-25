# 233. Number of Digit One

* *Difficulty: Hard*

* *Topics: Math*

* *Similar Questions:*

  * [Factorial Trailing Zeroes](factorial-trailing-zeroes.md)

  * [Digit Count in Range](digit-count-in-range.md)

## Problem:

<p>Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 13
<strong>Output:</strong> 6 
<strong>Explanation: </strong>Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
</pre>

## Solutions:

```c++
class Solution {
public:
    int countDigitOne(int n) {
        int origin = n;
        int ret = 0;
        int level = 0;
        int val = 1;
        while (n > 0) {
            int last = n % 10;
            if (last != 1) {
                ret += count(last, last * val, level);
            } else {
                ret += count(last, last * val, level);
                ret += (origin % (val) + 1);
            }
            level++;
            n /= 10;
            if (n > 0)
                val *= 10;
            
        }
        return ret;
    }
    
private:
    int count(int mostSig, int num, int level) {
        if (mostSig == 0)   return 0;
        if (mostSig == 1)  return num * 0.1 * level;
        return num * 0.1 * level + num / mostSig;
    }
    
};
```
