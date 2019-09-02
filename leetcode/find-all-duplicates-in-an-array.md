# 442. Find All Duplicates in an Array

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Find All Numbers Disappeared in an Array](find-all-numbers-disappeared-in-an-array.md)

## Problem:

<p>Given an array of integers, 1 &le; a[i] &le; <i>n</i> (<i>n</i> = size of array), some elements appear <b>twice</b> and others appear <b>once</b>.</p>

<p>Find all the elements that appear <b>twice</b> in this array.</p>

<p>Could you do it without extra space and in O(<i>n</i>) runtime?</p>
</p>
<p><b>Example:</b><br/>
<pre>
<b>Input:</b>
[4,3,2,7,8,2,3,1]

<b>Output:</b>
[2,3]
</pre>
## Solutions:

```c++
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ret;
        for (int i = 0; i < nums.size(); ++i) {
            int kickOut = 0;
            swap(kickOut, nums[i]);
            while (kickOut != 0 && nums[kickOut - 1] != kickOut) {
                swap(kickOut, nums[kickOut - 1]);
            }
            
            if (kickOut != 0) {
                ret.push_back(kickOut);
            }
        }
        
        return ret;
    }
};
```
