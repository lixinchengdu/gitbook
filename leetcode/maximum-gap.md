# 164. Maximum Gap

* *Difficulty: Hard*

* *Topics: Sort*

* *Similar Questions:*

## Problem:

<p>Given an unsorted array, find the maximum difference between the successive elements in its sorted form.</p>

<p>Return 0 if the array contains less than 2 elements.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,6,9,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The sorted form of the array is [1,3,6,9], either
&nbsp;            (3,6) or (6,9) has the maximum difference 3.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The array contains less than 2 elements, therefore return 0.</pre>

<p><b>Note:</b></p>

<ul>
	<li>You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.</li>
	<li>Try to solve it in linear time/space.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.size() < 2)    return 0;
        
        int n = nums.size();
        
        int minElement = INT_MAX;
        int maxElement = INT_MIN;
        
        for (auto num : nums) {
            minElement = min(minElement, num);
            maxElement = max(maxElement, num);
        }
        
        int bucketSize = (maxElement - minElement + 1 + n - 1 ) / n;
        vector<int> bucketMax (n, INT_MIN);
        vector<int> bucketMin (n, INT_MAX);
        
        for (auto num : nums) {
            int index = (num - minElement) / bucketSize;
            bucketMax[index] = max(bucketMax[index], num);
            bucketMin[index] = min(bucketMin[index], num);
        }
        
        int max_gap = 0;
        int prev_max = bucketMax[0];
        for (int i = 1; i < n; ++i) {
            if (bucketMin[i] != INT_MAX) {
                max_gap = max(max_gap, bucketMin[i] - prev_max);
                prev_max = bucketMax[i];
            }
        }
        
        return max_gap;
        
    }
};
```
