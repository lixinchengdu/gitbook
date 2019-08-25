# 57. Insert Interval

* *Difficulty: Hard*

* *Topics: Array, Sort*

* *Similar Questions:*

  * [Merge Intervals](merge-intervals.md)

  * [Range Module](range-module.md)

## Problem:

<p>Given a set of <em>non-overlapping</em> intervals, insert a new interval into the intervals (merge if necessary).</p>

<p>You may assume that the intervals were initially sorted according to their start times.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>Output:</strong> [[1,5],[6,9]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = <code>[[1,2],[3,5],[6,7],[8,10],[12,16]]</code>, newInterval = <code>[4,8]</code>
<strong>Output:</strong> [[1,2],[3,10],[12,16]]
<strong>Explanation:</strong> Because the new interval <code>[4,8]</code> overlaps with <code>[3,5],[6,7],[8,10]</code>.</pre>

<p><strong>NOTE:</strong>&nbsp;input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.</p>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> ret;
        int i = 0;
        for (; i < intervals.size(); ++i) {
            if (intervals[i][1] < newInterval[0])   {
                ret.push_back(intervals[i]);
            } else {
                break;
            }
        }
        
        if (i == intervals.size()) {
            ret.push_back(newInterval);
            return ret;
        }
        
        if (newInterval[1] < intervals[i][0]) {
            ret.push_back(newInterval);
            ret.push_back(intervals[i]);
        } else {
            ret.push_back({min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])});
        }
        
        ++i;
        
        for (; i < intervals.size(); ++i) {
            if (ret.back()[1] < intervals[i][0]) {
                ret.push_back(intervals[i]);
            } else {
                ret.back()[1] = max(ret.back()[1], intervals[i][1]);
            }
        }
        
        return ret;
        
    }
};
```
