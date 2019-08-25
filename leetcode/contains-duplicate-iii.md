# 220. Contains Duplicate III

* *Difficulty: Medium*

* *Topics: Sort, Ordered Map*

* *Similar Questions:*

  * [Contains Duplicate](contains-duplicate.md)

  * [Contains Duplicate II](contains-duplicate-ii.md)

## Problem:

<p>Given an array of integers, find out whether there are two distinct indices <i>i</i> and <i>j</i> in the array such that the <b>absolute</b> difference between <b>nums[i]</b> and <b>nums[j]</b> is at most <i>t</i> and the <b>absolute</b> difference between <i>i</i> and <i>j</i> is at most <i>k</i>.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[1,2,3,1]</span>, k = <span id="example-input-1-2">3</span>, t = <span id="example-input-1-3">0</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-2-1">[1,0,1,1]</span>, k = <span id="example-input-2-2">1</span>, t = <span id="example-input-2-3">2</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-3-1">[1,5,9,1,5,9]</span>, k = <span id="example-input-3-2">2</span>, t = <span id="example-input-3-3">3</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>
</div>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k < 0 || t < 0) return false;
        long kl = abs(k); // long! not int!
        long tl = abs(t); // long! not int!
        set<long> heap;
        int initHeapSize = min(long(nums.size()), kl);
    
        
        for (int i = 0; i < initHeapSize; ++i) {
            auto it = heap.lower_bound(nums[i] - tl);
            if (it != heap.end() && *it <= nums[i] + tl) return true; // if not using long, overflow happens.
            heap.insert(nums[i]);
        }
        
        for (int i = kl ; i < nums.size(); ++i) {
            auto it = heap.lower_bound(nums[i] - tl);
            if (it != heap.end() && *it - nums[i] <= tl) return true;
            heap.insert(nums[i]);
            heap.erase(nums[i - k]);
        }
        
        return false;
    }
};
```
