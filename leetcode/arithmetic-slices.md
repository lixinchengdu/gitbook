# 413. Arithmetic Slices

* *Difficulty: Medium*

* *Topics: Math, Dynamic Programming*

* *Similar Questions:*

  * [Arithmetic Slices II - Subsequence](arithmetic-slices-ii-subsequence.md)

## Problem:

<p>A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.</p>

<p>For example, these are arithmetic sequence:</p>
<pre>1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

<p>The following sequence is not arithmetic.</p> <pre>1, 1, 2, 5, 7</pre> 
<br/>

<p>A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.</p>

<p>A slice (P, Q) of array A is called arithmetic if the sequence:<br/>
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.</p>

<p>The function should return the number of arithmetic slices in the array A. </p>
<br/>

<p><b>Example:</b>
<pre>
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
</pre>
## Solutions:

```c++
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int count = 0;
        int right = 1;
        for (int i = 0; i < (int) A.size() - 2; ++i) { // minus!
            if (i + 1 == right) {
                while (right + 1 < A.size() && A[right + 1] - A[right] == A[right] - A[right - 1]) ++right;
            } 
            
            count += (right - i - 1);
            if (i + 1 == right) { // push right
                ++right;
            }
        }
        
        return count;
    }
};
```
