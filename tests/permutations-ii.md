# 47. Permutations II

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

  * [Next Permutation](./tests/permutations-ii.md)

  * [Permutations](./tests/permutations-ii.md)

  * [Palindrome Permutation II](./tests/permutations-ii.md)

  * [Number of Squareful Arrays](./tests/permutations-ii.md)

## Problem:

<p>Given a collection of numbers that might contain duplicates, return all possible unique permutations.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,1,2]
<strong>Output:</strong>
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    void recursion(vector<int>& num, int i, vector<vector<int> > &res, set<int>& visited) {
      
        if (i == num.size() - 1) {
            res.push_back(num);
            return;
        }
        
        set<int> visit;
        
        for (int k = i; k < num.size(); k++) {
            if (visit.count(num[k]) > 0)    continue;
            visit.insert(num[k]);
            swap(num[i], num[k]);
            recursion(num, i+1, res, visited);
            swap(num[i], num[k]);
        }
    }
    vector<vector<int> > permuteUnique(vector<int> &num) {
        //sort(num.begin(), num.end());
        vector<vector<int> >res;
        set<int> visited;
        recursion(num, 0, res, visited);
        return res;
    }
};
```
