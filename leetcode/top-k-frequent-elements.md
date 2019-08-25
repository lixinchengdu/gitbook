# 347. Top K Frequent Elements

* *Difficulty: Medium*

* *Topics: Hash Table, Heap*

* *Similar Questions:*

  * [Word Frequency](word-frequency.md)

  * [Kth Largest Element in an Array](kth-largest-element-in-an-array.md)

  * [Sort Characters By Frequency](sort-characters-by-frequency.md)

  * [Split Array into Consecutive Subsequences](split-array-into-consecutive-subsequences.md)

  * [Top K Frequent Words](top-k-frequent-words.md)

  * [K Closest Points to Origin](k-closest-points-to-origin.md)

## Problem:

<p>Given a non-empty array of integers, return the <b><i>k</i></b> most frequent elements.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[1,1,1,2,2,3]</span>, k = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">[1,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-2-1">[1]</span>, k = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">[1]</span></pre>
</div>

<p><b>Note: </b></p>

<ul>
	<li>You may assume <i>k</i> is always valid, 1 &le; <i>k</i> &le; number of unique elements.</li>
	<li>Your algorithm&#39;s time complexity <b>must be</b> better than O(<i>n</i> log <i>n</i>), where <i>n</i> is the array&#39;s size.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        for (auto num : nums) {
            ++counts[num];
        }
        
        set<pair<int, int>> topKIndex;
        
        for (auto it = counts.begin(); it != counts.end(); ++it) {
            topKIndex.insert({it->second, it->first});
            if (topKIndex.size() > k) {
                topKIndex.erase(topKIndex.begin());
            }
        }
        
        vector<int> ret;
        for (auto it = topKIndex.rbegin(); it != topKIndex.rend(); ++it) {
            ret.push_back(it->second);
        }
        
        return ret;
    }
private:
    unordered_map<int, int> counts;
};
```
