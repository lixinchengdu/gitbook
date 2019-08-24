# 303. Range Sum Query - Immutable

* *Difficulty: Easy*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Range Sum Query 2D - Immutable](./tests/range-sum-query-immutable.md)

  * [Range Sum Query - Mutable](./tests/range-sum-query-immutable.md)

  * [Maximum Size Subarray Sum Equals k](./tests/range-sum-query-immutable.md)

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
    NumArray(vector<int> &nums) {
    sum = 0;
    for (auto elem : nums)
    {
        sum += elem;
        sums.push_back(sum);
    }
    
    }

    int sumRange(int i, int j) {
        return sums[j] - sums[i-1];
        
    }
private:
    int sum = 0;
    vector <int> sums;
};


// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
```
