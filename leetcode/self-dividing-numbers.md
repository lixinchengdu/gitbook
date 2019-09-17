# 728. Self Dividing Numbers

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Perfect Number](perfect-number.md)

## Problem:

<p>
A <i>self-dividing number</i> is a number that is divisible by every digit it contains.
</p><p>
For example, 128 is a self-dividing number because <code>128 % 1 == 0</code>, <code>128 % 2 == 0</code>, and <code>128 % 8 == 0</code>.
</p><p>
Also, a self-dividing number is not allowed to contain the digit zero.
</p><p>
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
</p>
<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
left = 1, right = 22
<b>Output:</b> [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
</pre>
</p>

<p><b>Note:</b>
<li>The boundaries of each input argument are <code>1 <= left <= right <= 10000</code>.</li>
</p>
## Solutions:

```c++
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ret;
        for (int i = left; i <= right; ++i) {
            if (isSelfDivided(i)) {
                ret.push_back(i);
            }
        }
        
        return ret;
    }
    
private:
    bool isSelfDivided(int num) {
        int clone = num;
        while (clone > 0) {
            int digit = clone % 10;
            if (digit == 0) return false;
            clone /= 10;
            if (num % digit != 0)   return false;
        }
        
        return true;
    }
};
```
