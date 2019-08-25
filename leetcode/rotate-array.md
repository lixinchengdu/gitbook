# 189. Rotate Array

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

  * [Rotate List](rotate-list.md)

  * [Reverse Words in a String II](reverse-words-in-a-string-ii.md)

## Problem:

<p>Given an array, rotate the array to the right by <em>k</em> steps, where&nbsp;<em>k</em>&nbsp;is non-negative.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>[1,2,3,4,5,6,7]</code> and <em>k</em> = 3
<strong>Output:</strong> <code>[5,6,7,1,2,3,4]</code>
<strong>Explanation:</strong>
rotate 1 steps to the right: <code>[7,1,2,3,4,5,6]</code>
rotate 2 steps to the right: <code>[6,7,1,2,3,4,5]
</code>rotate 3 steps to the right: <code>[5,6,7,1,2,3,4]</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>[-1,-100,3,99]</code> and <em>k</em> = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.</li>
	<li>Could you do it in-place with O(1) extra space?</li>
</ul>
## Solutions:

```c++
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size();
        swap(nums, nums.size() - k, nums.size() -1);
        swap(nums, 0, nums.size() - k - 1);
        swap(nums, 0, nums.size() - 1); // it is nums.size() -1
        return;
    }
    
    void swap(vector<int>& nums, int left, int right) {
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
};
```
