# 163. Missing Ranges

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Summary Ranges](summary-ranges.md)

## Problem:

<p>Given a sorted integer array <strong><em>nums</em></strong>, where the range of elements are in the <strong>inclusive range</strong><b><strong> </strong>[<i>lower</i>, <i>upper</i>]</b>, return its missing ranges.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <strong><em>nums</em></strong> = <code>[0, 1, 3, 50, 75]</code>, <strong><i>lower</i></strong> = 0 and <strong><i>upper</i></strong> = 99,
<strong>Output:</strong> <code>[&quot;2&quot;, &quot;4-&gt;49&quot;, &quot;51-&gt;74&quot;, &quot;76-&gt;99&quot;]</code>
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<string> ret;
        int expected = lower;
        for (auto num : nums) {
            if (num <= expected) { // less and equal
                if (num == INT_MAX) return ret; // to prevent overflow
                expected = num + 1;
            } else {
                ret.push_back(missingRange(expected, num - 1));
                if (num == INT_MAX) return ret;
                expected = num + 1; // overflow
            }
        }
        
        if (expected <= upper) {
            ret.push_back(missingRange(expected, upper));
        }
        
        return ret;
    }
    
    string missingRange(int lower, int upper) {
        if (lower == upper) {
            return to_string(lower);
        } else {
            return to_string(lower) + "->" + to_string(upper);
        }
    }
};
```
