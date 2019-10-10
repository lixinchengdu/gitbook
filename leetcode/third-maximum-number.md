# 414. Third Maximum Number

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

  * [Kth Largest Element in an Array](kth-largest-element-in-an-array.md)

## Problem:

<p>Given a <b>non-empty</b> array of integers, return the <b>third</b> maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [3, 2, 1]

<b>Output:</b> 1

<b>Explanation:</b> The third maximum is 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1, 2]

<b>Output:</b> 2

<b>Explanation:</b> The third maximum does not exist, so the maximum (2) is returned instead.
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> [2, 2, 3, 1]

<b>Output:</b> 1

<b>Explanation:</b> Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int count = 0;
        int first = INT_MIN;
        int second = INT_MIN;
        int third = INT_MIN;
        
        for (auto& num : nums) {
            if ((count >= 1 && num == first) || (count >= 2 && num == second) || (count >= 3 && num == third))  continue;
            ++count;
            if (num >= first) {
                third = second;
                second = first;
                first = num;
            } else if (num >= second) {
                third = second;
                second = num;
            } else if (num >= third) {
                third = num;
            }
        }
        
        return count >= 3 ? third : first;
    }
};
```
