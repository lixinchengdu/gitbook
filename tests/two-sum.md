# 1. Two Sum

* *Difficulty: Easy*

* *Topics: Array, Hash Table*

* *Similar Questions:*

  * [3Sum](./tests/two-sum.md)

  * [4Sum](./tests/two-sum.md)

  * [Two Sum II - Input array is sorted](./tests/two-sum.md)

  * [Two Sum III - Data structure design](./tests/two-sum.md)

  * [Subarray Sum Equals K](./tests/two-sum.md)

  * [Two Sum IV - Input is a BST](./tests/two-sum.md)

  * [Two Sum Less Than K](./tests/two-sum.md)

## Problem:

<p>Given an array of integers, return <strong>indices</strong> of the two numbers such that they add up to a specific target.</p>

<p>You may assume that each input would have <strong><em>exactly</em></strong> one solution, and you may not use the <em>same</em> element twice.</p>

<p><strong>Example:</strong></p>

<pre>
Given nums = [2, 7, 11, 15], target = 9,

Because nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9,
return [<strong>0</strong>, <strong>1</strong>].
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numToIndex;
        for (int i = 0; i < nums.size(); ++i) {
            if (numToIndex.find(target - nums[i]) != numToIndex.end()) return {numToIndex[target - nums[i]], i};
            numToIndex[nums[i]] = i;
        }
    }
};
```
