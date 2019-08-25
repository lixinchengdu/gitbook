# 1. Two Sum

* *Difficulty: Easy*

* *Topics: Array, Hash Table*

* *Similar Questions:*

  * [3Sum](3sum.md)

  * [4Sum](4sum.md)

  * [Two Sum II - Input array is sorted](two-sum-ii-input-array-is-sorted.md)

  * [Two Sum III - Data structure design](two-sum-iii-data-structure-design.md)

  * [Subarray Sum Equals K](subarray-sum-equals-k.md)

  * [Two Sum IV - Input is a BST](two-sum-iv-input-is-a-bst.md)

  * [Two Sum Less Than K](two-sum-less-than-k.md)

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
            if (numToIndex.count(target - nums[i]) > 0) {
                return {numToIndex[target - nums[i]], i};
            }
            numToIndex[nums[i]] = i;
        }
        
        return {};
    }
};
```
