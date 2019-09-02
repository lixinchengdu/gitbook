# 560. Subarray Sum Equals K

* *Difficulty: Medium*

* *Topics: Array, Hash Table*

* *Similar Questions:*

  * [Two Sum](two-sum.md)

  * [Continuous Subarray Sum](continuous-subarray-sum.md)

  * [Subarray Product Less Than K](subarray-product-less-than-k.md)

  * [Find Pivot Index](find-pivot-index.md)

  * [Subarray Sums Divisible by K](subarray-sums-divisible-by-k.md)

## Problem:

<p>Given an array of integers and an integer <b>k</b>, you need to find the total number of continuous subarrays whose sum equals to <b>k</b>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>nums = [1,1,1], k = 2
<b>Output:</b> 2
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of the array is in range [1, 20,000].</li>
<li>The range of numbers in the array is [-1000, 1000] and the range of the integer <b>k</b> is [-1e7, 1e7].</li>
</ol>
</p>

## Solutions:

```c++
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int ret = 0;
        int sum = 0;
        unordered_map<int, int> valueCount;
        ++valueCount[sum];
        
        for (auto num : nums) {
            sum += num;
            int target = sum - k;
            if (valueCount.count(target) > 0) {
                ret += valueCount[target];
            }
            ++valueCount[sum];
        }
        
        return ret;
    }
};
```
