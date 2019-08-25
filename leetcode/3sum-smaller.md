# 259. 3Sum Smaller

* *Difficulty: Medium*

* *Topics: Array, Two Pointers*

* *Similar Questions:*

  * [3Sum](3sum.md)

  * [3Sum Closest](3sum-closest.md)

  * [Valid Triangle Number](valid-triangle-number.md)

  * [Two Sum Less Than K](two-sum-less-than-k.md)

## Problem:

<p>Given an array of <i>n</i> integers <i>nums</i> and a <i>target</i>, find the number of index triplets <code>i, j, k</code> with <code>0 &lt;= i &lt; j &lt; k &lt; n</code> that satisfy the condition <code>nums[i] + nums[j] + nums[k] &lt; target</code>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <i>nums</i> = <code>[-2,0,1,3]</code>, and <i>target</i> = 2
<strong>Output:</strong> 2 
<strong>Explanation:</strong>&nbsp;Because there are two triplets which sums are less than 2:
&nbsp;            [-2,0,1]
             [-2,0,3]
</pre>

<p><b style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">Follow up:</b> Could you solve it in <i>O</i>(<i>n</i><sup>2</sup>) runtime?</p>

## Solutions:

```c++
class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        if (nums.size() < 3)    return 0;
        sort(nums.begin(), nums.end());
        int ret = 0;
        
        for (int i = 0; i < nums.size() - 2; ++i) { // trap!
            int sum = target - nums[i];
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                if (nums[left] + nums[right] < sum) {
                    ret += right - left;
                    ++left;
                } else {
                    --right;
                }
            }
        }
        
        return ret;
    }
};
```
