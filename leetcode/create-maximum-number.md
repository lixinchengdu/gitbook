# 321. Create Maximum Number

* *Difficulty: Hard*

* *Topics: Dynamic Programming, Greedy*

* *Similar Questions:*

  * [Remove K Digits](remove-k-digits.md)

  * [Maximum Swap](maximum-swap.md)

## Problem:

<p>Given two arrays of length <code>m</code> and <code>n</code> with digits <code>0-9</code> representing two numbers. Create the maximum number of length <code>k &lt;= m + n</code> from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the <code>k</code> digits.</p>

<p><strong>Note: </strong>You should try to optimize your time and space complexity.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input:</strong>
nums1 = <code>[3, 4, 6, 5]</code>
nums2 = <code>[9, 1, 2, 5, 8, 3]</code>
k = <code>5</code>
<strong>Output:</strong>
<code>[9, 8, 6, 5, 3]</code></pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input:</strong>
nums1 = <code>[6, 7]</code>
nums2 = <code>[6, 0, 4]</code>
k = <code>5</code>
<strong>Output:</strong>
<code>[6, 7, 6, 0, 4]</code></pre>

<p><b>Example 3:</b></p>

<pre>
<strong>Input:</strong>
nums1 = <code>[3, 9]</code>
nums2 = <code>[8, 9]</code>
k = <code>3</code>
<strong>Output:</strong>
<code>[9, 8, 9]</code>
</pre>
## Solutions:

```c++
class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<int> ret;
        for (int i = 0; i <= nums1.size(); ++i) {
            int deleteNum1 = nums1.size() - i;
            int deleteNum2 = nums2.size() - (k - i);
            
            if (deleteNum1 < 0 || deleteNum2 < 0 || k - i < 0) continue; // sanity check
            
            vector<int> deleted1 = deleteDigit(nums1, deleteNum1);
            vector<int> deleted2 = deleteDigit(nums2, deleteNum2);
           
            vector<int> num = merge(deleted1, deleted2);
            ret = max(ret, num);
        }
       
        return ret;
    }

private:
    bool greater(vector<int>& num1, vector<int>& num2) { // it is not necessary to define it ourself
        for (int i = 0; i < min(num1.size(), num2.size()); ++i) {
            if (num1[i] > num2[i])  return true;
            if (num1[i] < num2[i])  return false;
        }
        
        return (num1.size() >= num2.size());
    }
    
    vector<int> deleteDigit(vector<int> nums, int k) {
        nums.push_back(10);
        vector<int> stk;
        
        for (auto& num : nums) {
            while (!stk.empty() && k > 0 && stk.back() < num) {
                stk.pop_back();
                --k;
            }
            stk.push_back(num);
        }
        
        stk.pop_back();
        return stk;
    }
    
    vector<int> merge(const vector<int> nums1, const vector<int> nums2) {
        vector<int> ans(nums1.size() + nums2.size());
        auto s1 = nums1.cbegin();
        auto e1 = nums1.cend();
        auto s2 = nums2.cbegin();
        auto e2 = nums2.cend();        
        int index = 0;
        while (s1 != e1 || s2 != e2)
            ans[index++] = 
              lexicographical_compare(s1, e1, s2, e2) ? *s2++ : *s1++;
        return ans;
    }
};
```
