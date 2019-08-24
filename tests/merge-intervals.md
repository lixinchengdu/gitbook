# 56. Merge Intervals

* *Difficulty: Medium*

* *Topics: Array, Sort*

* *Similar Questions:*

  * [Insert Interval](./tests/merge-intervals.md)

  * [Meeting Rooms](./tests/merge-intervals.md)

  * [Meeting Rooms II](./tests/merge-intervals.md)

  * [Teemo Attacking](./tests/merge-intervals.md)

  * [Add Bold Tag in String](./tests/merge-intervals.md)

  * [Range Module](./tests/merge-intervals.md)

  * [Employee Free Time](./tests/merge-intervals.md)

  * [Partition Labels](./tests/merge-intervals.md)

  * [Interval List Intersections](./tests/merge-intervals.md)

## Problem:

<p>Given a collection of intervals, merge all overlapping intervals.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [[1,4],[4,5]]
<strong>Output:</strong> [[1,5]]
<strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.</pre>

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
    vector<Interval> merge(vector<Interval>& intervals) {
        vector <Interval>   result;
        int n = intervals.size();
        if (n == 0) return result;
        vector <int>    startTimes;
        vector <int>    endTimes;
        for (auto interval: intervals)
        {
            startTimes.push_back(interval.start);
            endTimes.push_back(interval.end);
        }
        sort(startTimes.begin(), startTimes.end());
        sort(endTimes.begin(), endTimes.end());
        int startedCount = 0;
        int i = 0;
        int j = 0;
        int headTime = 0;
        while (i < startTimes.size() && j < endTimes.size())
        {
            if (startTimes[i] <= endTimes[j])
            {
                if (!startedCount)  headTime = startTimes[i];
                startedCount ++;
                i ++;
            }
            else
            {
                startedCount --;
                if (!startedCount)  {Interval mergedInterval = {headTime, endTimes[j]}; result.push_back(mergedInterval);}
                j++;
            }
        }
        Interval mergedInterval = {headTime, endTimes[endTimes.size()-1]};
        result.push_back(mergedInterval);
        return result;
    }
};
```
