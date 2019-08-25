# 239. Sliding Window Maximum

* *Difficulty: Hard*

* *Topics: Heap, Sliding Window*

* *Similar Questions:*

  * [Minimum Window Substring](minimum-window-substring.md)

  * [Min Stack](min-stack.md)

  * [Longest Substring with At Most Two Distinct Characters](longest-substring-with-at-most-two-distinct-characters.md)

  * [Paint House II](paint-house-ii.md)

## Problem:

<p>Given an array <em>nums</em>, there is a sliding window of size <em>k</em> which is moving from the very left of the array to the very right. You can only see the <em>k</em> numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <em>nums</em> = <code>[1,3,-1,-3,5,3,6,7]</code>, and <em>k</em> = 3
<strong>Output: </strong><code>[3,3,5,5,6,7] 
<strong>Explanation: 
</strong></code>
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong>Note: </strong><br />
You may assume <em>k</em> is always valid, 1 &le; k &le; input array&#39;s size for non-empty array.</p>

<p><strong>Follow up:</strong><br />
Could you solve it in linear time?</p>
## Solutions:

```c++
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> q;
        for (int i = 0; i < k - 1; ++i) {
            while (!q.empty() && q.back() < nums[i]) {
                q.pop_back();
            }
            q.push_back(nums[i]);
        }
        
        vector<int> ret;
        for (int i = k - 1; i < nums.size(); ++i) {
            int val = nums[i];
            while (!q.empty() && q.back() < val) {
                q.pop_back();
            }
            q.push_back(val);
            ret.push_back(q.front());
            if (nums[i - (k - 1)] == q.front()) {
                q.pop_front();
            }
        }
        
        return ret;
    }
};
```
