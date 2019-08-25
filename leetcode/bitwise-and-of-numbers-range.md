# 201. Bitwise AND of Numbers Range

* *Difficulty: Medium*

* *Topics: Bit Manipulation*

* *Similar Questions:*

## Problem:

<p>Given a range [m, n] where 0 &lt;= m &lt;= n &lt;= 2147483647, return the bitwise AND of all numbers in this range, inclusive.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [5,7]
<strong>Output:</strong> 4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [0,1]
<strong>Output:</strong> 0</pre>
## Solutions:

```c++
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int ret = 0;
        stack<int> mBitValues;
        stack<int> nBitValues;
        
        while (m > 0) {
            mBitValues.push(m&(-m));
            m -= m&(-m);
        }
        
        while (n > 0) {
            nBitValues.push(n&(-n));
            n -= n&(-n);
        }
        
        while (!mBitValues.empty() && !nBitValues.empty() && mBitValues.top() == nBitValues.top()) {
            ret += nBitValues.top();
            mBitValues.pop();
            nBitValues.pop();
        }
        
        return ret;
    }
};
```
