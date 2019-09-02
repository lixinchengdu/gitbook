# 402. Remove K Digits

* *Difficulty: Medium*

* *Topics: Stack, Greedy*

* *Similar Questions:*

  * [Create Maximum Number](create-maximum-number.md)

  * [Monotone Increasing Digits](monotone-increasing-digits.md)

## Problem:

<p>Given a non-negative integer <i>num</i> represented as a string, remove <i>k</i> digits from the number so that the new number is the smallest possible.
</p>

<p><b>Note:</b><br />
<ul>
<li>The length of <i>num</i> is less than 10002 and will be &ge; <i>k</i>.</li>
<li>The given <i>num</i> does not contain any leading zero.</li>
</ul>
</b>
</p>

<p><b>Example 1:</b>
<pre>
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
</pre>
</p>

<p><b>Example 2:</b>
<pre>
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
</pre>
</p>

<p><b>Example 3:</b>
<pre>
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    string removeKdigits(string num, int k) {
        vector<char> stk;
        num.push_back('0' - 1);
        for (auto& c : num) {
            while (k > 0 && !stk.empty() && stk.back() > c) {
                stk.pop_back();
                --k;
            }
            stk.push_back(c);
        }
        stk.pop_back();
        int start = 0;
        for (start = 0; start < stk.size() && stk[start] == '0'; ++start)  ;
        if (start == stk.size())    return "0";
        return string(stk.begin() + start, stk.end());        
    }
};
```
