# 315. Count of Smaller Numbers After Self

* *Difficulty: Hard*

* *Topics: Binary Search, Divide and Conquer, Sort, Binary Indexed Tree, Segment Tree*

* *Similar Questions:*

  * [Count of Range Sum](count-of-range-sum.md)

  * [Queue Reconstruction by Height](queue-reconstruction-by-height.md)

  * [Reverse Pairs](reverse-pairs.md)

## Problem:

<p>You are given an integer array <i>nums</i> and you have to return a new <i>counts</i> array. The <i>counts</i> array has the property where <code>counts[i]</code> is the number of smaller elements to the right of <code>nums[i]</code>.</p>

<p><b>Example:</b></p>

<pre>
<strong>Input:</strong> [5,2,6,1]
<strong>Output:</strong> <code>[2,1,1,0] 
<strong>Explanation:</strong></code>
To the right of 5 there are <b>2</b> smaller elements (2 and 1).
To the right of 2 there is only <b>1</b> smaller element (1).
To the right of 6 there is <b>1</b> smaller element (1).
To the right of 1 there is <b>0</b> smaller element.
</pre>
## Solutions:

```c++
class Solution {
public:
    class BIT {
        public:
            BIT(int upper) {
                nums.resize(upper + 1);
                upperBound = upper;
            }
        
            void add(int index) {
                while (index <= upperBound) {
                    ++nums[index];
                    index += lowerBit(index);
                }
            }
        
            int query(int index) {
                int sum = 0;
                while (index > 0) {
                    sum += nums[index];
                    index -= lowerBit(index);
                }
                return sum;
            }
        
            inline int lowerBit(int i) {
                return i & (-i);
            }
        
        private:
            int upperBound;
            vector<int> nums;
    };
    
    
    vector<int> countSmaller(vector<int>& nums) {
        if (nums.size() == 0)   return {};
        int smallest = *min_element(nums.begin(), nums.end());
        int offset = 0;
        if (smallest < 1) {
            offset = 1 - smallest; // offset is 1 not 0;
        }
        
        int upper = *max_element(nums.begin(), nums.end());
        BIT bit(upper+offset);
        int n = nums.size();
        vector<int> ret(n);
        for (int i = n - 1; i >= 0; --i) {
            int val = nums[i] + offset;
            ret[i] = bit.query(val-1); // query is tricky!
            bit.add(val);
        }
        
        return ret;
    }
      
};
```
