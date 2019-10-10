# 378. Kth Smallest Element in a Sorted Matrix

* *Difficulty: Medium*

* *Topics: Binary Search, Heap*

* *Similar Questions:*

  * [Find K Pairs with Smallest Sums](find-k-pairs-with-smallest-sums.md)

  * [Kth Smallest Number in Multiplication Table](kth-smallest-number-in-multiplication-table.md)

  * [Find K-th Smallest Pair Distance](find-k-th-smallest-pair-distance.md)

  * [K-th Smallest Prime Fraction](k-th-smallest-prime-fraction.md)

## Problem:

<p>Given a <i>n</i> x <i>n</i> matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.</p>

<p>
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
</p>

<p><b>Example:</b>
<pre>
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
</pre>
</p>

<p><b>Note: </b><br>
You may assume k is always valid, 1 &le; k &le; n<sup>2</sup>.</p>
## Solutions:

```c++
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int m = matrix.size();
        if (m == 0) return -1;
        int n = matrix[0].size();
        if (n == 0) return -1;
        
        int left = matrix[0][0]; 
        int right = matrix[m-1][n-1];
        
        while (left < right) {
            int mid = left + (right - left) / 2;
        
            int count = countSmallerNum(matrix, m, n, mid);
            if (count >= k) {
                right =  mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
    
private:
    int countSmallerNum(vector<vector<int>>& matrix, int m, int n, int num) {
        int row = m - 1;
        int col = 0;
        
        int count = 0;
        while (row >= 0 && col < n) {
            int product = matrix[row][col];
            if (product <= num) {
                count += row + 1;
                ++col;
            } else if (product > num) {
                --row;
            } 
        }
        
        return count;
    }
};

```
