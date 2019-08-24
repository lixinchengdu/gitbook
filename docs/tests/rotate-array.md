# 189. Rotate Array

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

  * [Rotate List](./tests/rotate-array.md)

  * [Reverse Words in a String II](./tests/rotate-array.md)

## Problem:

<p>Given an array, rotate the array to the right by <em>k</em> steps, where&nbsp;<em>k</em>&nbsp;is non-negative.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>[1,2,3,4,5,6,7]</code> and <em>k</em> = 3
<strong>Output:</strong> <code>[5,6,7,1,2,3,4]</code>
<strong>Explanation:</strong>
rotate 1 steps to the right: <code>[7,1,2,3,4,5,6]</code>
rotate 2 steps to the right: <code>[6,7,1,2,3,4,5]
</code>rotate 3 steps to the right: <code>[5,6,7,1,2,3,4]</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>[-1,-100,3,99]</code> and <em>k</em> = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.</li>
	<li>Could you do it in-place with O(1) extra space?</li>
</ul>
## Solutions:

```c++
class Solution {
public:
    int gcd (int a, int b) {
        if (b == 0) return a;
        return gcd(b, a%b);
    }
    
    
    void rotate(vector<int>& nums, int k) {
        int len = nums.size();
        if (len == 0)   return;
        if (k%len == 0) return;
        
        k = k % nums.size();
        int round = gcd(len,k);
        for (int i = 0; i < round; ++i) {
            int init = nums[i];
            int currentIndex = i;
            for (int count = 0; count < len/round - 1; ++count) {
                int nextIndex = (currentIndex - k + len) % len;
                nums[currentIndex] = nums[nextIndex];
                currentIndex = nextIndex;
            }
            nums[currentIndex] = init;
        }
        
    }
};
```
