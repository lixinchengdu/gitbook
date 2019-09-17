# 360. Sort Transformed Array

* *Difficulty: Medium*

* *Topics: Math, Two Pointers*

* *Similar Questions:*

  * [Squares of a Sorted Array](squares-of-a-sorted-array.md)

## Problem:

<p>Given a <b>sorted</b> array of integers <i>nums</i> and integer values <i>a</i>, <i>b</i> and <i>c</i>. Apply a quadratic function of the form f(<i>x</i>) = <i>ax</i><sup>2</sup> + <i>bx</i> + <i>c</i> to each element <i>x</i> in the array.</p>

<p>The returned array must be in <b>sorted order</b>.</p>

<p>Expected time complexity: <b>O(<i>n</i>)</b></p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[-4,-2,2,4]</span>, a = <span id="example-input-1-2">1</span>, b = <span id="example-input-1-3">3</span>, c = <span id="example-input-1-4">5</span>
<strong>Output: </strong><span id="example-output-1">[3,9,15,33]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-2-1">[-4,-2,2,4]</span>, a = <span id="example-input-2-2">-1</span>, b = <span id="example-input-2-3">3</span>, c = <span id="example-input-2-4">5</span>
<strong>Output: </strong><span id="example-output-2">[-23,-5,1,7]</span>
</pre>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        this->a = a;
        this->b = b;
        this->c = c;
        
        if (nums.size() == 0)   return {};
        if (a == 0) {
            if (b < 0) {
                reverse(nums.begin(), nums.end());
            }
            vector<int> ret;
            for (auto& val : nums) {
                ret.push_back(f(val));
            }
            
            return ret;
        }
        
        double vertex = -b / (double)(2 * a);
        
        int left = 0, right = nums.size() - 1; // largest value smaller than
        
        while (left < right) {
            int mid = right - (right - left) / 2;
            if (vertex <= nums[mid]) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        
        vector<int> ret;
        right = left + 1;
        while (left >= 0 && right < nums.size()) {
            if (abs(nums[left] - vertex) <= abs(nums[right] - vertex)) {
                ret.push_back(f(nums[left]));
                --left;
            } else {
                ret.push_back(f(nums[right]));
                ++right;
            }
        }
        
        if (left < 0) {
            while (right < nums.size()) {
                ret.push_back(f(nums[right++]));
            }
        }
        
        if (right >= nums.size()) {
            while (left >= 0) {
                ret.push_back(f(nums[left--]));
            }
        }
        
        if (a < 0) {
            reverse(ret.begin(), ret.end());
        }
        
        return ret;
    }
    
private:
    inline int f(int x) {
        return a * x * x + b * x + c;
    }
    
    int a;
    int b;
    int c;
    
};
```
