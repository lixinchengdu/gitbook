# 307. Range Sum Query - Mutable

* *Difficulty: Medium*

* *Topics: Binary Indexed Tree, Segment Tree*

* *Similar Questions:*

  * [Range Sum Query - Immutable](range-sum-query-immutable.md)

  * [Range Sum Query 2D - Mutable](range-sum-query-2d-mutable.md)

## Problem:

<p>Given an integer array <i>nums</i>, find the sum of the elements between indices <i>i</i> and <i>j</i> (<i>i</i> &le; <i>j</i>), inclusive.</p>

<p>The <i>update(i, val)</i> function modifies <i>nums</i> by updating the element at index <i>i</i> to <i>val</i>.</p>

<p><b>Example:</b></p>

<pre>
Given nums = [1, 3, 5]

sumRange(0, 2) -&gt; 9
update(1, 2)
sumRange(0, 2) -&gt; 8
</pre>

<p><b>Note:</b></p>

<ol>
	<li>The array is only modifiable by the <i>update</i> function.</li>
	<li>You may assume the number of calls to <i>update</i> and <i>sumRange</i> function is distributed evenly.</li>
</ol>

## Solutions:

```c++
class NumArray {
public:
    NumArray(vector<int>& nums) {
        int n = nums.size();
        bits = vector<int> (n+1 , 0);
        this->nums = vector<int> (n, 0); // don't reuse the name
        for (int i = 0; i < nums.size(); ++i) {
            update(i, nums[i]);
        }
    }
    
    void update(int i, int val) {
        int diff = val - nums[i];
        nums[i] = val;
        add(i + 1, diff);
    }
    
    void add(int i, int diff) {
        while (i <= nums.size()) {
            bits[i] += diff;
            i += lowbit(i);
        }
    }
    
    int sum(int i) {
        int sum = 0;
        while (i > 0) {
            sum += bits[i];
            i -= lowbit(i);
        }
        return sum;
    }
    
    int sumRange(int i, int j) {
        return sum(j + 1) - sum(i);
    }
    
    inline int lowbit(int i) {
        return i & (-i);
    }
    
private:
    vector<int> bits;
    vector<int> nums;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */
```
