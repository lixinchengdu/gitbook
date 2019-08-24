# 238. Product of Array Except Self

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Trapping Rain Water](./tests/product-of-array-except-self.md)

  * [Maximum Product Subarray](./tests/product-of-array-except-self.md)

  * [Paint House II](./tests/product-of-array-except-self.md)

## Problem:

<p>Given an array <code>nums</code> of <em>n</em> integers where <em>n</em> &gt; 1, &nbsp;return an array <code>output</code> such that <code>output[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code>.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b>  <code>[1,2,3,4]</code>
<b>Output:</b> <code>[24,12,8,6]</code>
</pre>

<p><strong>Note: </strong>Please solve it <strong>without division</strong> and in O(<em>n</em>).</p>

<p><strong>Follow up:</strong><br />
Could you solve it with constant space complexity? (The output array <strong>does not</strong> count as extra space for the purpose of space complexity analysis.)</p>

## Solutions:

```c++
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector <int> result(n, 1);
        if (!n) return result;
        vector<int> forward(n, 1);
        vector<int> backward(n, 1);
        //cout << "aha!" << endl;
        for (int i = 1; i < n; i++)
        {
            forward[i] = forward[i-1] * nums[i-1];
        }
        //cout << "ad" << endl;
        for (int i = n-2; i >= 0; i--)
        {
            backward[i] = backward[i+1] * nums[i+1];
        }
        //cout << "asdfadg" << endl;
        for (int i = 0; i < n; i++)
        {
            result[i] = forward[i]*backward[i];
        }
       // cout << "adf" << endl;
        return result;
    }
};
```
