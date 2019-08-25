# 280. Wiggle Sort

* *Difficulty: Medium*

* *Topics: Array, Sort*

* *Similar Questions:*

  * [Sort Colors](sort-colors.md)

  * [Wiggle Sort II](wiggle-sort-ii.md)

## Problem:

<p>Given an unsorted array <code>nums</code>, reorder it <b>in-place</b> such that <code>nums[0] &lt;= nums[1] &gt;= nums[2] &lt;= nums[3]...</code>.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>nums = [3,5,2,1,6,4]</code>
<b>Output:</b> One possible answer is [3,5,1,6,2,4]</pre>

## Solutions:

```c++
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        for (int i = 1; i < nums.size(); ++i) {
            if (i % 2 == 1) {
                if (nums[i] < nums[i - 1]) {
                    swap(nums[i], nums[i-1]);
                }
            } else {
                if (nums[i] > nums[i-1]) {
                    swap(nums[i], nums[i-1]);
                }
            }
        }
    }
};
```
