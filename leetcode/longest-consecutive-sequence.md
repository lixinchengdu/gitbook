# 128. Longest Consecutive Sequence

* *Difficulty: Hard*

* *Topics: Array, Union Find*

* *Similar Questions:*

  * [Binary Tree Longest Consecutive Sequence](binary-tree-longest-consecutive-sequence.md)

## Problem:

<p>Given an unsorted array of integers, find the length of the longest consecutive elements sequence.</p>

<p>Your algorithm should run in O(<em>n</em>) complexity.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;[100, 4, 200, 1, 3, 2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

## Solutions:

```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet (nums.begin(), nums.end());
        
        int ret = 0;
        
        for (auto num : nums) {
            if (numSet.count(num) > 0) {
                int count = 1;
                count += countToward(numSet, num - 1, true);
                count += countToward(numSet, num + 1, false);
                ret = max(ret, count);
            }
        }
        
        return ret;
    }
    
    int countToward(unordered_set<int>& numSet, int num, bool backward) {
        int count = 0;
        while (true) {
            auto it = numSet.find(num);
            if (it == numSet.end()) return count;
            ++count;
            numSet.erase(it);
            if (backward)
                --num;
            else 
                ++num;
        }
    }
    
    
};
```
