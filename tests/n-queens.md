# 51. N-Queens

* *Difficulty: Hard*

* *Topics: Backtracking*

* *Similar Questions:*

  * [N-Queens II](./tests/n-queens.md)

  * [Grid Illumination](./tests/n-queens.md)

## Problem:

<p>The <em>n</em>-queens puzzle is the problem of placing <em>n</em> queens on an <em>n</em>&times;<em>n</em> chessboard such that no two queens attack each other.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/8-queens.png" style="width: 258px; height: 276px;" /></p>

<p>Given an integer <em>n</em>, return all distinct solutions to the <em>n</em>-queens puzzle.</p>

<p>Each solution contains a distinct board configuration of the <em>n</em>-queens&#39; placement, where <code>&#39;Q&#39;</code> and <code>&#39;.&#39;</code> both indicate a queen and an empty space respectively.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 4
<strong>Output:</strong> [
 [&quot;.Q..&quot;,  // Solution 1
  &quot;...Q&quot;,
  &quot;Q...&quot;,
  &quot;..Q.&quot;],

 [&quot;..Q.&quot;,  // Solution 2
  &quot;Q...&quot;,
  &quot;...Q&quot;,
  &quot;.Q..&quot;]
]
<strong>Explanation:</strong> There exist two distinct solutions to the 4-queens puzzle as shown above.
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        solveNQueensHelper (n, 0);
        return result;
    }
    
private:
    vector <vector <string> >   result;
    vector <int> path;
    void solveNQueensHelper (int n, int pos)
    {
        if (isConflict(path))   return;
        //cout << "aha!" << endl;
        if (pos == n)   {result.push_back(printQueens(path));   return;}
        for (int i = 0; i < n; i++)
        {
            path.push_back(i);
            solveNQueensHelper (n, pos + 1);
            path.pop_back();
        }
    }
    bool isConflict (vector <int>& path)
    {
        int n = path.size();
        if (n == 0) return false;
        int lastPosition = path.back();
        //cout << "head:";
        // printVector(path);
        for (int i = 0; i < n-1; i++)
        {
           // printVector(path);
            if (path[i] == lastPosition || path[i] == lastPosition - (n-1-i) ||  path[i] == lastPosition + (n-1-i) )
                {
                    /*
                cout << "zhe"<< endl; 
                cout << lastPosition << endl;
                cout << lastPosition - (n-1-i) << endl;
                int x = (lastPosition - (n-1-i) >= 0 && path[lastPosition - (n-1-i)] == lastPosition)? 1:0;
                cout << x << endl;
                cout << lastPosition + (n-1-i) << endl;
                int y = (lastPosition + (n-1-i) <= path.size()-1 && path[lastPosition + (n-1-i)] == lastPosition)? 1:0;
                cout << y << endl;
                */
                return true;}
        }
        //cout << "after:"; printVector(path);
        return false;
    }
    
    vector <string> printQueens(vector <int> path)
    {
        int n = path.size();
        vector <string> strResult (n, string(n,'.'));
        if (n == 0) {return strResult;}
        for (int i = 0; i < n; i++)
        {
            strResult[i][path[i]] = 'Q';
        }
        return strResult;
    }
    
    void printVector (vector <int>& v)
    {
        for (int n: v)
        {
            cout << n << " ";
        }
        cout << endl;
    }
    
};
```
