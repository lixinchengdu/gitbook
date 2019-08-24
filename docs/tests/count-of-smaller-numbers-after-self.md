# 315. Count of Smaller Numbers After Self

* *Difficulty: Hard*

* *Topics: Binary Search, Divide and Conquer, Sort, Binary Indexed Tree, Segment Tree*

* *Similar Questions:*

  * [Count of Range Sum](./tests/count-of-smaller-numbers-after-self.md)

  * [Queue Reconstruction by Height](./tests/count-of-smaller-numbers-after-self.md)

  * [Reverse Pairs](./tests/count-of-smaller-numbers-after-self.md)

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
class BIT {
public:
    BIT(int n): n_(n), data_(n+1, 0) {}
        
    void add(int i, int val) {
        while (i <= n_) {
            data_[i] += val;
            i += lowbit(i);
        }
    }
    
    int query(int i) {
        int sum = 0;
        while (i > 0) {
            sum += data_[i];
            i -= lowbit(i);
        }
        return sum;
    }
        
private:
    inline int lowbit(int i) {
        return i & -i;
    }
    vector<int> data_;
    int n_;
};


class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> discretes (nums.begin(), nums.end());
        sort(discretes.begin(), discretes.end());
        auto it = unique(discretes.begin(), discretes.end());
        discretes.resize(distance(discretes.begin(), it));
        unordered_map<int, int> discretesID;
        for (int i = 0; i < discretes.size(); ++i) {
            discretesID[discretes[i]] = i + 1;
        }
        
        BIT bit(discretes.size());
        
        vector<int> ret;
        
        for (auto it = nums.rbegin(); it != nums.rend(); ++it) {
            int num = *it;
            int ID = discretesID[num];
            int count = bit.query(ID - 1);
            ret.push_back(count);
            bit.add(ID, 1);
        }
        
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
```
