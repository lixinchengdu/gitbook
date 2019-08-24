# 90. Subsets II

* *Difficulty: Medium*

* *Topics: Array, Backtracking*

* *Similar Questions:*

  * [Subsets](./tests/subsets-ii.md)

## Problem:

<p>Given a collection of integers that might contain duplicates, <strong><em>nums</em></strong>, return all possible subsets (the power set).</p>

<p><strong>Note:</strong> The solution set must not contain duplicate subsets.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,2,2]
<strong>Output:</strong>
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector <vector <int> > result;
        vector <int> path;
        Helper (nums, 0, path, result);
        return result;
    }
    
    void Helper (vector<int>& nums, int start, vector<int>& path, vector <vector <int> >& result)
    {
        int n = nums.size();
        if (start >= n)
        {
            result.push_back(path);
            return;
        }
        int end = start + 1;
        int startNum = nums[start];
        while (end < n && nums[end] == startNum)
        {
            end++;
        }
        for (int i = 0; i <= end - start; ++i)
        {
            auto back = path.end();
           // cout << startNum << endl;
            path.insert(back, i, startNum);
            //path.push_back(startNum);
           // cout << "aha!" <<endl;
            Helper (nums, end, path, result);
            path.erase(path.end()-i, path.end());
        }
    }
};
```
