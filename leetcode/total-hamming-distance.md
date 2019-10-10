# 477. Total Hamming Distance

* *Difficulty: Medium*

* *Topics: Bit Manipulation*

* *Similar Questions:*

  * [Hamming Distance](hamming-distance.md)

## Problem:

<p>The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.</p>

<p>Now your job is to find the total Hamming distance between all pairs of the given numbers.</p>


<p><b>Example:</b><br />
<pre>
<b>Input:</b> 4, 14, 2

<b>Output:</b> 6

<b>Explanation:</b> In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>Elements of the given array are in the range of <code>0 </code> to <code>10^9</code>
<li>Length of the array will not exceed <code>10^4</code>. </li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int oneCount[32] = {0};
        for (auto num : nums) {
            for (int i = 0; i < 32; ++i) {
                if ((num & (0x1 << i)) != 0) {
                    ++oneCount[i];
                }
            }
        }
        
        int ret = 0;
        int n = nums.size();
        
        for (int i = 0; i < 32; ++i) {
            ret += oneCount[i] * (n - oneCount[i]);
        }
        
        return ret;
        
    }
};
```
