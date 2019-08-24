# 179. Largest Number

* *Difficulty: Medium*

* *Topics: Sort*

* *Similar Questions:*

## Problem:

<p>Given a list of non negative integers, arrange them such that they form the largest number.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>[10,2]</code>
<strong>Output:</strong> &quot;<code>210&quot;</code></pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>[3,30,34,5,9]</code>
<strong>Output:</strong> &quot;<code>9534330&quot;</code>
</pre>

<p><strong>Note:</strong> The result may be very large, so you need to return a string instead of an integer.</p>

## Solutions:

```c++
bool strCmp (const string& str1, const string& str2) {
    string xy = str1 + str2;
    string yx = str2 + str1;
    return xy > yx;
}

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> numStrs;
        for (auto num : nums) {
            numStrs.push_back(to_string(num));
        }
        sort(numStrs.begin(), numStrs.end(), strCmp);
        
        if (numStrs[0] == "0")  return "0";
        
        string ret;
        for (auto numStr: numStrs) {
            ret.append(numStr);
        }
        return ret;
    }
};
```
