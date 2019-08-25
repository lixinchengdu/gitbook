# 204. Count Primes

* *Difficulty: Easy*

* *Topics: Hash Table, Math*

* *Similar Questions:*

  * [Ugly Number](ugly-number.md)

  * [Ugly Number II](ugly-number-ii.md)

  * [Perfect Squares](perfect-squares.md)

## Problem:

<p>Count the number of prime numbers less than a non-negative number, <b><i>n</i></b>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>

## Solutions:

```c++
class Solution {
public:
    int countPrimes(int n) {
        if (n <= 1) return 0;
        vector<bool> valid(n, true);
        
        for (int i = 2; i <= sqrt(n); ++i) {
            if (!valid[i]) continue;
            for (int j = i * 2; j < n; j = j + i) {
                valid[j] = false;
            }
        }
        
        int count = 0;
        
        for (int i = 2; i < n; ++i) {
            if (valid[i]) ++count;
        }
        
        return count;
    }
};
```
