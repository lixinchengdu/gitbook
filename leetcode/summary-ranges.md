# 228. Summary Ranges

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Missing Ranges](missing-ranges.md)

  * [Data Stream as Disjoint Intervals](data-stream-as-disjoint-intervals.md)

## Problem:

<p>Given a sorted integer array without duplicates, return the summary of its ranges.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b>  [0,1,2,4,5,7]
<b>Output:</b> [&quot;0-&gt;2&quot;,&quot;4-&gt;5&quot;,&quot;7&quot;]
<strong>Explanation: </strong>0,1,2 form a continuous range;&nbsp;4,5 form a continuous range.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b>  [0,2,3,4,6,8,9]
<b>Output:</b> [&quot;0&quot;,&quot;2-&gt;4&quot;,&quot;6&quot;,&quot;8-&gt;9&quot;]
<strong>Explanation: </strong>2,3,4 form a continuous range;&nbsp;8,9 form a continuous range.
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        auto ranges = helper(nums, 0, nums.size() - 1);
        vector<string> ret;
        for (auto& range : ranges) {
            ret.push_back(toString(range));
        }
        return ret;
    }
    
    vector<pair<int, int>> helper(vector<int>& nums, int left, int right) {
        if (left > right)   return {};
        if (long(nums[right]) == long(nums[left]) + right - left) {
            return {{nums[left], nums[right]}};
        }
        
        int mid = left + (right - left) / 2;
        auto leftRange = helper(nums, left, mid);
        auto rightRange = helper(nums, mid + 1, right);
        
        if (!leftRange.empty() && !rightRange.empty()) {
            auto leftLast = leftRange.back();
            leftRange.pop_back();
            if (leftLast.second + 1 == rightRange[0].first) {
                rightRange[0].first = leftLast.first;
            } else {
                leftRange.push_back(leftLast);
            }
        }
        
        leftRange.insert(leftRange.end(), rightRange.begin(), rightRange.end());
        return leftRange;
    }
    
    inline string toString(pair<int, int> range) {
        return range.first == range.second ? to_string(range.first) : to_string(range.first) + "->" + to_string(range.second);
    }
};
```
