# 665. Non-decreasing Array

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

## Problem:

<p>
Given an array with <code>n</code> integers, your task is to check if it could become non-decreasing by modifying <b>at most</b> <code>1</code> element.
</p>

<p>
We define an array is non-decreasing if <code>array[i] <= array[i + 1]</code> holds for every <code>i</code> (1 <= i < n).
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [4,2,3]
<b>Output:</b> True
<b>Explanation:</b> You could modify the first <code>4</code> to <code>1</code> to get a non-decreasing array.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [4,2,1]
<b>Output:</b> False
<b>Explanation:</b> You can't get a non-decreasing array by modify at most one element.
</pre>
</p>

<p><b>Note:</b>
The <code>n</code> belongs to [1, 10,000].
</p>
## Solutions:

```c++
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        if (nums.size() <= 1)   return true;
        int p = -1;
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] > nums[i+1]) {
                if (p != -1)    return false;
                else {
                    p = i;
                }
            }
        }
        
        return p == -1 || p == 0 || p == nums.size() - 2 || nums[p-1] <= nums[p+1] || nums[p] <= nums[p+2];
        
    }
};
```
