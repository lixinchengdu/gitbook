# 398. Random Pick Index

* *Difficulty: Medium*

* *Topics: Reservoir Sampling*

* *Similar Questions:*

  * [Linked List Random Node](linked-list-random-node.md)

  * [Random Pick with Blacklist](random-pick-with-blacklist.md)

  * [Random Pick with Weight](random-pick-with-weight.md)

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
    Solution(vector<int>& nums) {
        this->nums = nums;
    }
    
    int pick(int target) {
        int count = 0;
        int ret;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != target)  continue;
            ++count;
            if (rand() % count == 0) {
                ret = i;
            }
        }
        
        return ret;
    }
    
private:
    vector<int> nums;
    
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
```
