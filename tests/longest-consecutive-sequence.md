# 128. Longest Consecutive Sequence

* *Difficulty: Hard*

* *Topics: Array, Union Find*

* *Similar Questions:*

  * [Binary Tree Longest Consecutive Sequence](./tests/longest-consecutive-sequence.md)

## Problem:

<p>Given an unsorted array of integers, find the length of the longest consecutive elements sequence.</p>

<p>Your algorithm should run in O(<em>n</em>) complexity.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;[100, 4, 200, 1, 3, 2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

## Solutions:

```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int maxConsec = 1;
        int n = nums.size();
        if (!n) return 0;
        unordered_map <int, int> num2index;
       // UF uf(n);
        for (int i = 0; i < n; i++)
        {
            if (num2index.count(nums[i]) == 0)
                num2index[nums[i]] = i;
        }
        UF uf(n);
        for (auto num:nums)
        {
            //cout << num << endl;
            if (num2index.count(num-1) > 0)
            {
                int index1 = num2index[num];
                int index2 = num2index[num-1];
                maxConsec = max(maxConsec, uf.unionCombine(index1, index2));
            }
            if (num2index.count(num+1) > 0)
            {
                int index1 = num2index[num];
                int index2 = num2index[num+1];
                maxConsec = max(maxConsec, uf.unionCombine(index1, index2));
            }
        }
        return maxConsec;
    }
    
    
class UF
{
    public:
        UF(int n): count(n)
        {
            id = new int[n];
            sz = new int[n];
            for (int i = 0; i < n; i++)
            {
                id[i] = i;
                sz[i] = 1;
            }
        }
        ~UF()
        {
            delete[] id;
            delete[] sz;
        }
        
        int find (int p)
        {
            while (p != id[p]) 
            {
                id[p] = id[id[p]];
                p = id[p];
            }
            return p;
        }
        
        bool connected(int p, int q)
        {
            return find(p) == find(q);
        }
        
        int unionCombine(int p, int q)
        {
          // cout << "here" << endl;
            //cout << p << " " <<q << endl;
           // if (p == 2 || q == 0)   cout << "fuck" << endl;
            int result;
            int ancP = find(p);
            int ancQ = find(q);
            if (ancP == ancQ)   return sz[ancP];
            if (sz[ancP] > sz[ancQ])
            {
                id[ancQ] = ancP;
                sz[ancP] += sz[ancQ]; 
                result = sz[ancP];
            }
            else
            {
                id[ancP] = ancQ;
                sz[ancQ] += sz[ancP];
                result = sz[ancQ];
            }
            count --;
            return result;
        }
        
        int getCount()
        {
            return count;
        }
        
        void decreaseCount()
        {
            count --;
        }
        
    private:
        int* id;
        int count;
        int* sz;
};
    
};
```
