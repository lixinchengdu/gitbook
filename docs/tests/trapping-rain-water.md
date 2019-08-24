# 42. Trapping Rain Water

* *Difficulty: Hard*

* *Topics: Array, Two Pointers, Stack*

* *Similar Questions:*

  * [Container With Most Water](./tests/trapping-rain-water.md)

  * [Product of Array Except Self](./tests/trapping-rain-water.md)

  * [Trapping Rain Water II](./tests/trapping-rain-water.md)

  * [Pour Water](./tests/trapping-rain-water.md)

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
        int n = height.size();
        if (!n) return 0;
        vector <int> tallest(n, 0);
        int maxHeight = INT_MIN;
        for (int i = 0; i < n; ++i)
        {
            maxHeight = max(maxHeight, height[i]);
            tallest[i] = maxHeight;
        }
        maxHeight = INT_MIN;
        for (int i = n-1; i >= 0; --i)
        {
            maxHeight = max(maxHeight, height[i]);
            tallest[i] = min(tallest[i], maxHeight);
        }
        
        int count = 0;
        for (int i = 0; i < n; ++i)
        {
            count += tallest[i] - height[i];
        }
        
        return count;
        
    }
};
```
