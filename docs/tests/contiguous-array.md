# 525. Contiguous Array

* *Difficulty: Medium*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Maximum Size Subarray Sum Equals k](./tests/contiguous-array.md)

## Problem:

<p>Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. </p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [0,1]
<b>Output:</b> 2
<b>Explanation:</b> [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [0,1,0]
<b>Output:</b> 2
<b>Explanation:</b> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>
</p>

<p><b>Note:</b>
The length of the given binary array will not exceed 50,000.
</p>
## Solutions:

```c++
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size();
        unordered_map <int ,int>  sum2index;
        //sum2index[0] = -1;
        int sum = 0;
        for (int i = -1; i < n-1; i++)
        {
            if (sum2index.find(sum) == sum2index.end())
            {
                sum2index[sum] = i;
            }
            sum += nums[i+1]? 1 : -1;
        }
        sum = 0;
        int maxLen = 0;
        for (int i = 0; i < n; i++)
        {
            sum += nums[i]? 1:-1;
            if (sum2index.find(sum) != sum2index.end())
            {
                maxLen = max(maxLen, i - sum2index[sum] );
            }
        }
        return maxLen;
    }
};
```
