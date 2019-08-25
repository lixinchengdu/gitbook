# 611. Valid Triangle Number

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [3Sum Smaller](3sum-smaller.md)

## Problem:

Given an array consists of non-negative integers,  your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [2,2,3,4]
<b>Output:</b> 3
<b>Explanation:</b>
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of the given array won't exceed 1000.</li>
<li>The integers in the given array are in the range of [0, 1000].</li>
</ol>
</p>

## Solutions:

```c++
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        if (nums.size() < 3)    return 0;
        sort(nums.begin(), nums.end());
        int count = 0;
        
        for (int i = 0; i < nums.size() - 2; ++i) {
            int a = nums[i];
            int bIndex = i + 1;
            int cIndex = i + 2;
            
            for (; cIndex < nums.size(); ++cIndex) {
                while (bIndex < cIndex && a + nums[bIndex] <= nums[cIndex]) {
                    ++bIndex;
                }
                
                if (cIndex > bIndex) {
                    count += (cIndex - bIndex);
                }
            }
        }
        
        return count;
    }
};
```
