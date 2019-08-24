# 204. Count Primes

* *Difficulty: Easy*

* *Topics: Hash Table, Math*

* *Similar Questions:*

  * [Ugly Number](./tests/count-primes.md)

  * [Ugly Number II](./tests/count-primes.md)

  * [Perfect Squares](./tests/count-primes.md)

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
        if (n == 1) return 0;
        vector<bool> isPrimeArray(n, true);
        int largestPrimeNum = 2;
        bool goFurther = true;
        while (goFurther) {
            goFurther = false;
            for (int i = 2; i * largestPrimeNum < n; ++i) {
                isPrimeArray[i * largestPrimeNum] = false;
            }
            for (int i = largestPrimeNum + 1; i < n; ++i) {
                if (isPrimeArray[i]) {
                    largestPrimeNum = i;
                    goFurther = true;
                    break;
                }
            }
        }
        int cnt = 0;
        for (int i = 2; i < n; ++i) {
            if (isPrimeArray[i])    ++cnt;
        }
        return cnt;
    }
};
```
