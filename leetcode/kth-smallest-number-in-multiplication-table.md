# 668. Kth Smallest Number in Multiplication Table

* *Difficulty: Hard*

* *Topics: Binary Search*

* *Similar Questions:*

  * [Kth Smallest Element in a Sorted Matrix](kth-smallest-element-in-a-sorted-matrix.md)

  * [Find K-th Smallest Pair Distance](find-k-th-smallest-pair-distance.md)

  * [K-th Smallest Prime Fraction](k-th-smallest-prime-fraction.md)

## Problem:

<p>
Nearly every one have used the <a href="https://en.wikipedia.org/wiki/Multiplication_table">Multiplication Table</a>. But could you find out the <code>k-th</code> smallest number quickly from the multiplication table?
</p>

<p>
Given the height <code>m</code> and the length <code>n</code> of a <code>m * n</code> Multiplication Table, and a positive integer <code>k</code>, you need to return the <code>k-th</code> smallest number in this table.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> m = 3, n = 3, k = 5
<b>Output:</b> 
<b>Explanation:</b> 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> m = 2, n = 3, k = 6
<b>Output:</b> 
<b>Explanation:</b> 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The <code>m</code> and <code>n</code> will be in the range [1, 30000].</li>
<li>The <code>k</code> will be in the range [1, m * n]</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        int left = 1; 
        int right = m * n;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
        
            int count = countSmallerNum(m, n, mid);
            if (count >= k) {
                right =  mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
    
private:
    int countSmallerNum(int m, int n, int num) {
        int row = m - 1;
        int col = 0;
        
        int count = 0;
        while (row >= 0 && col < n) {
            int product = (row + 1) * (col + 1);
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
