# 217. Contains Duplicate

* *Difficulty: Easy*

* *Topics: Array, Hash Table*

* *Similar Questions:*

  * [Contains Duplicate II](contains-duplicate-ii.md)

  * [Contains Duplicate III](contains-duplicate-iii.md)

## Problem:

<p>Given an array of integers, find if the array contains any duplicates.</p>

<p>Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,1]
<strong>Output:</strong> true</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[1,2,3,4]
<strong>Output:</strong> false</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>[1,1,1,3,3,4,3,2,4,2]
<strong>Output:</strong> true</pre>

## Solutions:

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> numSet;
        for (auto num : nums) {
            if (numSet.count(num) > 0) {
                return true;
            }
            numSet.insert(num);
        }
        
        return false;
    }
};
```
