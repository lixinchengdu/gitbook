# 238. Product of Array Except Self

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Trapping Rain Water](trapping-rain-water.md)

  * [Maximum Product Subarray](maximum-product-subarray.md)

  * [Paint House II](paint-house-ii.md)

## Problem:

<p>Given an array <code>nums</code> of <em>n</em> integers where <em>n</em> &gt; 1, &nbsp;return an array <code>output</code> such that <code>output[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code>.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b>  <code>[1,2,3,4]</code>
<b>Output:</b> <code>[24,12,8,6]</code>
</pre>

<p><strong>Note: </strong>Please solve it <strong>without division</strong> and in O(<em>n</em>).</p>

<p><strong>Follow up:</strong><br />
Could you solve it with constant space complexity? (The output array <strong>does not</strong> count as extra space for the purpose of space complexity analysis.)</p>

## Solutions:

```c++
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ret (n, 1);
        
        for (int i = n - 2; i >= 0; --i) {
            ret[i] *= ret[i + 1] * nums[i + 1];
        }
        
        int product = 1;
        for (int i = 0; i < n; ++i) {
            ret[i] *= product;
            product *= nums[i];
        }
        
        return ret;
    }
};
```
