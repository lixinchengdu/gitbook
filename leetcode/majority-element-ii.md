# 229. Majority Element II

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Majority Element](majority-element.md)

  * [Check If a Number Is Majority Element in a Sorted Array](check-if-a-number-is-majority-element-in-a-sorted-array.md)

## Problem:

<p>Given an integer array of size <i>n</i>, find all elements that appear more than <code>&lfloor; n/3 &rfloor;</code> times.</p>

<p><strong>Note: </strong>The algorithm should run in linear time and in O(1) space.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,2,3]
<strong>Output:</strong> [3]</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,1,1,3,3,2,2,2]
<strong>Output:</strong> [1,2]</pre>

## Solutions:

```c++
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int majorityVal[2];
        int majorityCount[2] {0, 0};
        
        for (auto& num : nums) { // pay attention to the order of the series of if statements
            if (majorityCount[0] == 0) {
                majorityVal[0] = num;
                majorityCount[0] = 1;
            } else if (num == majorityVal[0]) {
                ++majorityCount[0];
            } else if (majorityCount[1] == 0) {
                majorityVal[1] = num;
                majorityCount[1] = 1;
            } else if (num == majorityVal[1]) {
                ++majorityCount[1];
                if (majorityCount[1] > majorityCount[0]) {
                    swap(majorityCount[0], majorityCount[1]);
                    swap(majorityVal[0], majorityVal[1]);
                }
            } else {
                --majorityCount[0];
                --majorityCount[1];
            }
        }
        
        majorityCount[0] = 0;
        majorityCount[1] = 0;
        for (auto& num : nums) {
            if (majorityVal[0] == num) {
                ++majorityCount[0];
            } else if (majorityVal[1] == num) {
                ++majorityCount[1];
            }
        }
    
        
        vector<int> ret;
        if (majorityCount[0] > nums.size() / 3) {
            ret.push_back(majorityVal[0]);
        }
        
        if (majorityCount[1] > nums.size() / 3) {
            ret.push_back(majorityVal[1]);
        }
        
        return ret;
    }
};
```
