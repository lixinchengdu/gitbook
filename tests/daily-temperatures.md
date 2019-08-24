# 739. Daily Temperatures

* *Difficulty: Medium*

* *Topics: Hash Table, Stack*

* *Similar Questions:*

  * [Next Greater Element I](./tests/daily-temperatures.md)

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
    struct record {
        int temperature;
        int index;
        record(int temperature, int index) {
            this->temperature = temperature;
            this->index = index;
        }
    };
    
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int len = temperatures.size();
        stack<record> stk;
        vector<int> ret (len, 0);
        for (int i = 0; i < temperatures.size(); ++i) {
            if (stk.empty()) {
                stk.emplace(temperatures[i], i);
            } else if (stk.top().temperature >= temperatures[i]) {
                stk.emplace(temperatures[i], i);
            } else {
                while (!stk.empty() && stk.top().temperature < temperatures[i]) {
                    ret[stk.top().index] = i - stk.top().index;
                    stk.pop();
                }
                stk.emplace(temperatures[i], i);
            }
        }
        return ret;
    }
};
```
