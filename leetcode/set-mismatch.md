# 645. Set Mismatch

* *Difficulty: Easy*

* *Topics: Hash Table, Math*

* *Similar Questions:*

  * [Find the Duplicate Number](find-the-duplicate-number.md)

## Problem:

<p>
The set <code>S</code> originally contains numbers from 1 to <code>n</code>. But unfortunately, due to the data error, one of the numbers in the set got duplicated to <b>another</b> number in the set, which results in repetition of one number and loss of another number. 
</p>

<p>
Given an array <code>nums</code> representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> nums = [1,2,2,4]
<b>Output:</b> [2,3]
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The given array size will in the range [2, 10000].</li>
<li>The given array's numbers won't have any order.</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int dup, miss;
        for (auto& num : nums) {
            if (nums[abs(num) - 1] < 0) {
                dup = abs(num);
            } else {
                nums[abs(num) - 1] *= -1;
            }
        }
        
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) {
                miss = i + 1;
                break;
            }
        }
        
        return {dup, miss};
        
    }
};
```
