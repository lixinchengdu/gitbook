# 303. Range Sum Query - Immutable

* *Difficulty: Easy*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Range Sum Query 2D - Immutable](range-sum-query-2d-immutable.md)

  * [Range Sum Query - Mutable](range-sum-query-mutable.md)

  * [Maximum Size Subarray Sum Equals k](maximum-size-subarray-sum-equals-k.md)

## Problem:

<p>Given an integer array <i>nums</i>, find the sum of the elements between indices <i>i</i> and <i>j</i> (<i>i</i> &le; <i>j</i>), inclusive.</p>

<p><b>Example:</b><br>
<pre>
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>You may assume that the array does not change.</li>
<li>There are many calls to <i>sumRange</i> function.</li>
</ol>
</p>
## Solutions:

```c++
class NumArray {
public:
    NumArray(vector<int>& nums) {
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            prefixSum.push_back(sum);
        }
    }
    
    int sumRange(int i, int j) {
        if (i == 0) return prefixSum[j];
        return prefixSum[j] - prefixSum[i - 1];
    }
    
private:
    vector<int> prefixSum;
    
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
```
