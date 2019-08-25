# 167. Two Sum II - Input array is sorted

* *Difficulty: Easy*

* *Topics: Array, Two Pointers, Binary Search*

* *Similar Questions:*

  * [Two Sum](two-sum.md)

  * [Two Sum IV - Input is a BST](two-sum-iv-input-is-a-bst.md)

  * [Two Sum Less Than K](two-sum-less-than-k.md)

## Problem:

<p>Given an array of integers that is already <strong><em>sorted in ascending order</em></strong>, find two numbers such that they add up to a specific target number.</p>

<p>The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Your returned answers (both index1 and index2) are not zero-based.</li>
	<li>You may assume that each input would have <em>exactly</em> one solution and you may not use the <em>same</em> element twice.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> numbers = [2,7,11,15], target = 9
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.</pre>

## Solutions:

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;
        while (left < right) {
            if (numbers[left] + numbers[right] == target)   return {left + 1, right + 1};
            else if (numbers[left] + numbers[right] < target) {
                ++left;
            } else {
                --right;
            }
        }
        
        return {0, 0};
    }
};
```
