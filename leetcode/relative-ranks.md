# 506. Relative Ranks

* *Difficulty: Easy*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>
Given scores of <b>N</b> athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [5, 4, 3, 2, 1]
<b>Output:</b> ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
<b>Explanation:</b> The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". <br/>For the left two athletes, you just need to output their relative ranks according to their scores.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>N is a positive integer and won't exceed 10,000.</li>
<li>All the scores of athletes are guaranteed to be unique.</li>
</ol>
</p>

## Solutions:

```c++
class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        vector<pair<int, int>> v;
        for (int i = 0; i < nums.size(); ++i) {
            v.push_back({nums[i], i});
        }
        
        string medals[3] = {
            "Gold Medal",
            "Silver Medal",
            "Bronze Medal"
        };
        
        sort(v.begin(), v.end(), greater<pair<int, int>>());
        vector<string> ret (v.size());
        
        for (int i = 0; i < min(3, (int)v.size()); ++i) {
            ret[v[i].second] = medals[i];
        }
        
        for (int i = 3; i < v.size(); ++i) {
            ret[v[i].second] = to_string(i+1);
        }
        
        return ret;
    }
};
```
