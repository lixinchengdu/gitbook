# 42. Trapping Rain Water

* *Difficulty: Hard*

* *Topics: Array, Two Pointers, Stack*

* *Similar Questions:*

  * [Container With Most Water](container-with-most-water.md)

  * [Product of Array Except Self](product-of-array-except-self.md)

  * [Trapping Rain Water II](trapping-rain-water-ii.md)

  * [Pour Water](pour-water.md)

## Problem:

<p>Given <em>n</em> non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;" /><br />
<small>The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. <strong>Thanks Marcos</strong> for contributing this image!</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6</pre>

## Solutions:

```c++
class Solution {
public:
    int trap(vector<int>& height) {
        int ret = 0;
        int leftHeight = 0;
        int rightHeight = 0;
        int left = 0;
        int right = height.size() - 1;
        while (left <= right) {
            if (height[left] <= height[right]) {
                if (leftHeight - height[left] > 0)  ret += leftHeight - height[left];
                leftHeight = max(leftHeight, height[left]);
                ++left;
            } else {
                if (rightHeight - height[right] > 0) {
                    if (rightHeight - height[right] > 0)    ret += rightHeight - height[right];
                }
                rightHeight = max(rightHeight, height[right]);
                --right;
            }
        }
        
        return ret;
        
    }
};
```
