# 398. Random Pick Index

* *Difficulty: Medium*

* *Topics: Reservoir Sampling*

* *Similar Questions:*

  * [Linked List Random Node](./tests/random-pick-index.md)

  * [Random Pick with Blacklist](./tests/random-pick-index.md)

  * [Random Pick with Weight](./tests/random-pick-index.md)

## Problem:

<p>Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.</p>

<p><b>Note:</b><br />
The array size can be very large. Solution that uses too much extra space will not pass the judge.</p>

<p><b>Example:</b></p>

<pre>
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
</pre>

## Solutions:

```c++
class Solution {
public:
    Solution(vector<int> nums): v(nums) {
        
    }
    
    int pick(int target) {
        int i = rand()%v.size();
        while(1)
        {
            if (v[i] == target) return i;
            i = rand()%v.size();
        }
    }
    
private:
    vector <int> v;

};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
```
