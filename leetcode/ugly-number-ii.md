# 264. Ugly Number II

* *Difficulty: Medium*

* *Topics: Math, Dynamic Programming, Heap*

* *Similar Questions:*

  * [Merge k Sorted Lists](merge-k-sorted-lists.md)

  * [Count Primes](count-primes.md)

  * [Ugly Number](ugly-number.md)

  * [Perfect Squares](perfect-squares.md)

  * [Super Ugly Number](super-ugly-number.md)

## Problem:

<p>Write a program to find the <code>n</code>-th ugly number.</p>

<p>Ugly numbers are<strong> positive numbers</strong> whose prime factors only include <code>2, 3, 5</code>.&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 12
<strong>Explanation: </strong><code>1, 2, 3, 4, 5, 6, 8, 9, 10, 12</code> is the sequence of the first <code>10</code> ugly numbers.</pre>

<p><strong>Note: </strong>&nbsp;</p>

<ol>
	<li><code>1</code> is typically treated as an ugly number.</li>
	<li><code>n</code> <b>does not exceed 1690</b>.</li>
</ol>
## Solutions:

```c++
class Solution {
public:
    struct UglyNumber{
        int val;
        int prime;
        int index;
        
        UglyNumber(int val, int prime, int index) {
            this->val = val;
            this->prime = prime;
            this->index = index;
        }
        
        bool operator>(const UglyNumber& other) const {
            return val*prime > other.val*other.prime;
        } 
    };
    
    int nthUglyNumber(int n) {
        vector<int> primes {2, 3, 5}; 
        vector<int> dp(n, 0);
        dp[0] = 1;
        priority_queue<UglyNumber, vector<UglyNumber>, greater<UglyNumber>> pq;
        for (auto prime : primes) {
            pq.push({1, prime, 0});
        }
        
        for (int i = 1; i < n; ++i) {
            do {
                UglyNumber ugly = pq.top(); pq.pop();
                dp[i] = ugly.val * ugly.prime;
                pq.push({dp[ugly.index + 1], ugly.prime, ugly.index + 1});
            } while (pq.top().val * pq.top().prime == dp[i]);
            
        }
        
        return dp[n-1];
    }
};
```
