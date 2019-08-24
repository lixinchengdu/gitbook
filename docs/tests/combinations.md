# 77. Combinations

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

  * [Combination Sum](./tests/combinations.md)

  * [Permutations](./tests/combinations.md)

## Problem:

<p>Given two integers <em>n</em> and <em>k</em>, return all possible combinations of <em>k</em> numbers out of 1 ... <em>n</em>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;n = 4, k = 2
<strong>Output:</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int> > combine(int n, int k) {
        vector<vector<int>> result;
        if(k>n) return result;
        if (k==1)
        {
            for (int i=1; i<=n; i++)
            {
                vector<int> tmp;
                tmp.push_back(i);
                result.push_back(tmp);
            }
            return result;
        }
        vector<vector<int>> tmp1=combine(n-1,k);
        vector<vector<int>> tmp2=combine(n-1,k-1);
         for (vector <vector <int>>::iterator vvIt=tmp1.begin(); vvIt!=tmp1.end(); vvIt++)
        {
            result.push_back(*vvIt);
        }
        for (vector <vector <int>>::iterator vvIt=tmp2.begin(); vvIt!= tmp2.end(); vvIt++)
        {
            vector<int> inter;
            
            for(vector<int>::iterator vIt=(*vvIt).begin(); vIt!=(*vvIt).end(); vIt++)
            {
                inter.push_back(*vIt);
            }
            inter.push_back(n);
            result.push_back(inter);
        }
       
        return result;
    }
};
```
