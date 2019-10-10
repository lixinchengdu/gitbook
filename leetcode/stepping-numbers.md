# 1151. Stepping Numbers

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

## Problem:

<p>A <em>Stepping Number</em> is&nbsp;an integer&nbsp;such that&nbsp;all of its adjacent digits have an absolute difference of exactly <code>1</code>. For example, <code>321</code> is a Stepping Number while <code>421</code> is not.</p>

<p>Given two integers <code>low</code> and <code>high</code>, find and return a <strong>sorted</strong> list of all the Stepping Numbers in the range <code>[low, high]</code>&nbsp;inclusive.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> low = 0, high = 21
<strong>Output:</strong> [0,1,2,3,4,5,6,7,8,9,10,12,21]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= low &lt;= high &lt;= 2 * 10^9</code></li>
</ul>

## Solutions:

```c++
class Solution {
public:
    vector<int> countSteppingNumbers(int low, int high) {
        vector<int> ret;
        if (low <= 0 && high >= 0)  ret.push_back(0);
        for (int i = 1; i <= 9; ++i) {
            dfs(i, low, high, ret);
        }
        
        sort(ret.begin(), ret.end());
        
        return ret;
    }
    
    
private:
    void dfs(int num, int low, int high, vector<int>& ret) {
        if (num > high) return;
        if (num >= low) {
            ret.push_back(num);
        }
        
        int lastDigit = num % 10;
        if (lastDigit - 1 >= 0 && num < INT_MAX / 10) {
            dfs(num * 10 + (lastDigit - 1), low, high, ret);
        }
        
        if (lastDigit + 1 <= 9 && num < INT_MAX / 10) {
            dfs(num * 10 + (lastDigit + 1), low, high, ret);
        }
    }
    
};
```
