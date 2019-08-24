# 307. Range Sum Query - Mutable

* *Difficulty: Medium*

* *Topics: Binary Indexed Tree, Segment Tree*

* *Similar Questions:*

  * [Range Sum Query - Immutable](./tests/range-sum-query-mutable.md)

  * [Range Sum Query 2D - Mutable](./tests/range-sum-query-mutable.md)

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
    NumArray(vector<int> nums): numVector(nums.size()+1, 0), _nums(nums) {
        length = nums.size()+1;
        for (int i = 0; i < length-1; i++)
        {
            update(i, nums[i]);
        }
    }
    
    void update(int i, int val) {
        int diff = val - sumRange(i,i); 
        i += 1;
        while (i < length)
        {
            numVector[i] += diff;
            i += lowbit(i);
        }
    }
    
    int sumRange(int i, int j) {
        i++;
        j++;
        return getSum(j) - getSum(i-1);
    }
    
    int getSum(int i)
    {
        int sum = 0;
        while (i > 0)
        {
            sum += numVector[i];
            i -= lowbit(i);
        }
        return sum;
    }
    
private:
    
    vector <int> numVector;
    vector <int> _nums;
    int length;
    inline int lowbit(int x)
    {
        return x&(-x);
    }
    
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
```
