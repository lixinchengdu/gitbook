# 260. Single Number III

* *Difficulty: Medium*

* *Topics: Bit Manipulation*

* *Similar Questions:*

  * [Single Number](single-number.md)

  * [Single Number II](single-number-ii.md)

## Problem:

<p>Given an array of numbers <code>nums</code>, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>  <code>[1,2,1,3,2,5]</code>
<strong>Output:</strong> <code>[3,5]</code></pre>

<p><b>Note</b>:</p>

<ol>
	<li>The order of the result is not important. So in the above example, <code>[5, 3]</code> is also correct.</li>
	<li>Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?</li>
</ol>
## Solutions:

```c++
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int digest = 0;
        for (auto& num : nums) {
            digest ^= num;
        }
        
        // String from the least significant bit, the first bit set to 1 
        digest &= (-digest);
        vector<int> ret(2, 0);

        for (auto& num : nums) {
            if (num & digest) {
                ret[0] ^= num;
            } else {
                ret[1] ^= num;
            }
        }
        return ret;
    }
};
```
