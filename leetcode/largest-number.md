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
class Solution {
public:
    struct comparator {
        bool operator()(const string& a, const string& b) {
            return a + b > b + a; // not necessary to have stol;
        }
    };
    
    string largestNumber(vector<int>& nums) {
        
        vector<string> numStr;
        
        bool allZeros = true;
        
        for (auto num : nums) {
            if (num != 0)   allZeros = false;
            numStr.push_back(to_string(num));
        }
        
        if (allZeros == true)   return "0";
        
        sort(numStr.begin(), numStr.end(), comparator());
        string ret;
        for (auto& str : numStr) {
            ret.append(str);
        }
        
        return ret;
    }
};
```
