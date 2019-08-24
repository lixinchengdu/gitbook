# 386. Lexicographical Numbers

* *Difficulty: Medium*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Given an integer <i>n</i>, return 1 - <i>n</i> in lexicographical order.</p>

<p>For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].</p>

<p>Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.</p>

## Solutions:

```c++
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        if (n < 10)
        {
            for (int i = 1; i <= n; i ++)
            {
                result.push_back(i);
            }
            return result;
        }
        for (int i = 1; i < 10; i++)
            lexicalOrderHelper (i, n);
        return result;
        
    }
    
private:
    vector <int> result;
   // int path;
    void lexicalOrderHelper (int path, int n)
    {
        if (path > n)   return;
        result.push_back(path);
        for (int i = 0; i < 10; i++)
        {
            lexicalOrderHelper ( path*10+i, n);
           // path = path/10;
        }
    }
    
};
```
