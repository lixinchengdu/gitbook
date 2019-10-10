# 594. Longest Harmonious Subsequence

* *Difficulty: Easy*

* *Topics: Hash Table*

* *Similar Questions:*

## Problem:

<p>We define a harmounious array as an array where the difference between its maximum value and its minimum value is <b>exactly</b> 1.</p>

<p>Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible <a href="https://en.wikipedia.org/wiki/Subsequence">subsequences</a>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [1,3,2,2,5,2,3,7]
<b>Output:</b> 5
<b>Explanation:</b> The longest harmonious subsequence is [3,2,2,2,3].
</pre>

<p>&nbsp;</p>

<p><b>Note:</b> The length of the input array will not exceed 20,000.</p>

## Solutions:

```c++
class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> numCount;
        for (auto& num : nums) {
            ++numCount[num];
        }
        
        int ret = 0;
        for (auto& entry : numCount) {
            if (numCount.count(entry.first + 1)) {
                ret = max(ret, entry.second + numCount[entry.first + 1]);
            }
        }
        
        return ret;
        
    }
};
```
