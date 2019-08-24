# 59. Spiral Matrix II

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Spiral Matrix](./tests/spiral-matrix-ii.md)

## Problem:

<p>Given a positive integer <em>n</em>, generate a square matrix filled with elements from 1 to <em>n</em><sup>2</sup> in spiral order.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong>
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector <vector <int>> myvector (n, vector <int> (n) );
        if (n == 0)
            return myvector;
        int counter = 1;
        int counterSnapshot = 0;
        int xIndex = 0;
        int yIndex = -1;
        int method = 0; 
        while (counterSnapshot != counter)
        {   
            counterSnapshot = counter;
            switch (method)
            {
                case 0: 
                    while (1)
                    {
                       
                       if ( yIndex+1 < n && myvector[xIndex][yIndex+1] == 0 )
                            yIndex ++;
                        else
                            break;
                        myvector[xIndex][yIndex] = counter++;
                    }
                    break;
                case 1:
                    while (1)
                    {
                       
                        if (xIndex + 1 < n && myvector[xIndex+1][yIndex] == 0)
                            xIndex ++;
                        else
                            break; 
                        myvector[xIndex][yIndex] = counter++;
                    }
                    break;
                case 2:
                    while (1)
                    {
                        
                        if (yIndex-1 >= 0 && myvector[xIndex][yIndex-1] == 0)
                            yIndex --;
                        else
                            break;
                        myvector[xIndex][yIndex] = counter ++;
                    }
                    break;
                case 3:
                    while (1)
                    {
                        
                        if (xIndex-1 >= 0 && myvector[xIndex-1][yIndex] == 0)
                            xIndex --;
                        else
                            break;
                        myvector[xIndex][yIndex] = counter ++;
                    }
                    break;
            }
            method += 1;
            method %= 4;
        }
        return myvector;
    }
};
```
