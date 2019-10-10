# 581. Shortest Unsorted Continuous Subarray

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

## Problem:

<p>Given an integer array, you need to find one <b>continuous subarray</b> that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too. </p> 

<p>You need to find the <b>shortest</b> such subarray and output its length.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [2, 6, 4, 8, 10, 9, 15]
<b>Output:</b> 5
<b>Explanation:</b> You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>Then length of the input array is in range [1, 10,000].</li>
<li>The input array may contain duplicates, so ascending order here means <b><=</b>. </li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        if (nums.size() == 0)   return 0;
        vector<int> copy = nums;
        sort(copy.begin(), copy.end());
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right && nums[left] == copy[left])  ++left;
        while (left <= right && nums[right] == copy[right]) --right;
        
        return right - left + 1;
        
        
    }
};
```
