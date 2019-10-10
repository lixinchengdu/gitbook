# 628. Maximum Product of Three Numbers

* *Difficulty: Easy*

* *Topics: Array, Math*

* *Similar Questions:*

  * [Maximum Product Subarray](maximum-product-subarray.md)

## Problem:

<p>Given an integer array, find three numbers whose product is maximum and output the maximum product.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [1,2,3]
<b>Output:</b> 6
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [1,2,3,4]
<b>Output:</b> 24
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The length of the given array will be in range [3,10<sup>4</sup>] and all elements are in the range [-1000, 1000].</li>
	<li>Multiplication of any three numbers in the input won&#39;t exceed the range of 32-bit signed integer.</li>
</ol>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        vector<int> pos;
        vector<int> neg;
        
        for (auto& num : nums) {
            if (num >= 0) {
                pos.push_back(num);
            } else {
                neg.push_back(num);
            }
        }
        
        sort(pos.begin(), pos.end());
        sort(neg.begin(), neg.end());
        
        int ret = INT_MIN;
        if (neg.size() >= 3) {
            ret = max(ret, neg[neg.size() - 1] * neg[neg.size() - 2] * neg[neg.size() - 3]);
        }
        if (neg.size() >= 2 && pos.size() >= 1) {
            ret = max(ret, neg[0] * neg[1] * pos.back());
        }
        if (neg.size() >=1 && pos.size() >= 2) {
            ret = max(ret, neg.back() * pos[0] * pos[1]);
        }
        if (pos.size() >= 3) {
            ret = max(ret, pos[pos.size() - 1] * pos[pos.size() - 2] * pos[pos.size() - 3]);
        }
        
        return ret;
        
    }
};
```
