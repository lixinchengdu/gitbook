# 57. Insert Interval

* *Difficulty: Hard*

* *Topics: Array, Sort*

* *Similar Questions:*

  * [Merge Intervals](./tests/insert-interval.md)

  * [Range Module](./tests/insert-interval.md)

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
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        vector <Interval> result;
        int start = newInterval.start, end = newInterval.end;
        bool flag = true;
        if (intervals.size() > 0 && newInterval.end < intervals[0].start)
        {
            result.push_back(newInterval);
            flag = false;
        }
        for (auto interval : intervals)
        {
            if (interval.end < newInterval.start)
            {
                result.push_back(interval);
                continue;
            }
            else if (interval.start > newInterval.end)
            {
                if (flag)
                {
                    Interval mergedInterval(start, end);
                    result.push_back(mergedInterval);
                    flag = false;
                }
                result.push_back(interval);
                continue;
            }
            else
            {
                start = min(interval.start, start);
                end = max(interval.end, end);
            }
        }
        if (flag)
        {
                    Interval mergedInterval(start, end);
                    result.push_back(mergedInterval);
                    flag = false;
        }
        
        
       // if (intervals.size() > 0 && newInterval.start > intervals.back().end)
    //    {
      //      result.push_back(newInterval);
        //}
        
        return result;
    }
};
```
