# 219. Contains Duplicate II

* *Difficulty: Easy*

* *Topics: Array, Hash Table*

* *Similar Questions:*

  * [Contains Duplicate](contains-duplicate.md)

  * [Contains Duplicate III](contains-duplicate-iii.md)

## Problem:

<p>Given an array of integers and an integer <i>k</i>, find out whether there are two distinct indices <i>i</i> and <i>j</i> in the array such that <b>nums[i] = nums[j]</b> and the <b>absolute</b> difference between <i>i</i> and <i>j</i> is at most <i>k</i>.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[1,2,3,1]</span>, k = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-2-1">[1,0,1,1]</span>, k = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-3-1">[1,2,3,1,2,3]</span>, k = <span id="example-input-3-2">2</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>
</div>
</div>
</div>

## Solutions:

```c++
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> valToIndex;
        for (int i = 0; i < nums.size(); ++i) {
            if (valToIndex.count(nums[i]) > 0 && i - valToIndex[nums[i]] <= k) {
                return true;
            }
            
            valToIndex[nums[i]] = i;
        }
        
        return false;
    }
};
```
