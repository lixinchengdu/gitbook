# 442. Find All Duplicates in an Array

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Find All Numbers Disappeared in an Array](./tests/find-all-duplicates-in-an-array.md)

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
            //if (nums[nums[i]-1] == nums[i])   continue;
            int cur = nums[i];
            nums[i] = -1;
            
            while (nums[cur-1] != -1 && nums[cur-1] != cur) {
                swap(nums[cur-1], cur);
            }
            
            if (nums[cur-1] == -1) {
                nums[cur-1] = cur;
            } else if (nums[cur-1] == cur) {
                ret.push_back(cur);
            }
            
            
        }
        sort(ret.begin(), ret.end());
        return ret;
    }
};
```
