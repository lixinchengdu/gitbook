# 283. Move Zeroes

* *Difficulty: Easy*

* *Topics: Array, Two Pointers*

* *Similar Questions:*

  * [Remove Element](./tests/move-zeroes.md)

## Problem:

<p>Given an array <code>nums</code>, write a function to move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>[0,1,0,3,12]</code>
<b>Output:</b> <code>[1,3,12,0,0]</code></pre>

<p><b>Note</b>:</p>

<ol>
	<li>You must do this <b>in-place</b> without making a copy of the array.</li>
	<li>Minimize the total number of operations.</li>
</ol>
## Solutions:

```c++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 0) {
                ++count;
            } else {
                nums[i - count] = nums[i];
            }
        }
        for (int i = nums.size() - count; i < nums.size(); ++i) {
            nums[i] = 0;
        }
    }
};
```
