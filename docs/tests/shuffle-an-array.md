# 384. Shuffle an Array

* *Difficulty: Medium*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Shuffle a set of numbers without duplicates.
</p>

<p><b>Example:</b>
<pre>
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    Solution(vector<int> nums) {
        data_ = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return data_;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> ret = data_;
        if (ret.size() == 0)    return ret;
        for (int i = ret.size() - 1; i >= 1 ; --i) {
           
            int targetIndex = rand() % (i + 1);
            swap(ret[i], ret[targetIndex]);
        }
        return ret;
    }
    
    vector<int> data_;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */
```
