# 739. Daily Temperatures

* *Difficulty: Medium*

* *Topics: Hash Table, Stack*

* *Similar Questions:*

  * [Next Greater Element I](next-greater-element-i.md)

## Problem:

<p>
Given a list of daily temperatures <code>T</code>, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.  If there is no future day for which this is possible, put <code>0</code> instead.
</p><p>
For example, given the list of temperatures <code>T = [73, 74, 75, 71, 69, 72, 76, 73]</code>, your output should be <code>[1, 1, 4, 2, 1, 1, 0, 0]</code>.
</p>

<p><b>Note:</b>
The length of <code>temperatures</code> will be in the range <code>[1, 30000]</code>.
Each temperature will be an integer in the range <code>[30, 100]</code>.
</p>
## Solutions:

```c++
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int n = T.size();
        vector<int> ret(n, 0);
        stack<int> stk;
        
        for (int i = 0; i < T.size(); ++i) {
            while (!stk.empty() && T[stk.top()] < T[i]) {
                ret[stk.top()] = i - stk.top();
                stk.pop();
            }
            
            stk.push(i);
        }
        
        return ret;
    }
};
```
