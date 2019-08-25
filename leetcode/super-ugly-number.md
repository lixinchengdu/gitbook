# 313. Super Ugly Number

* *Difficulty: Medium*

* *Topics: Math, Heap*

* *Similar Questions:*

  * [Ugly Number II](ugly-number-ii.md)

## Problem:

<p>Write a program to find the <code>n<sup>th</sup></code> super ugly number.</p>

<p>Super ugly numbers are positive numbers whose all prime factors are in the given prime list <code>primes</code> of size <code>k</code>.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> n = 12, <code>primes</code> = <code>[2,7,13,19]</code>
<b>Output:</b> 32 
<strong>Explanation: </strong><code>[1,2,4,7,8,13,14,16,19,26,28,32] </code>is the sequence of the first 12 
             super ugly numbers given <code>primes</code> = <code>[2,7,13,19]</code> of size 4.</pre>

<p><b>Note:</b></p>

<ul>
	<li><code>1</code> is a super ugly number for any given <code>primes</code>.</li>
	<li>The given numbers in <code>primes</code> are in ascending order.</li>
	<li>0 &lt; <code>k</code> &le; 100, 0 &lt; <code>n</code> &le; 10<sup>6</sup>, 0 &lt; <code>primes[i]</code> &lt; 1000.</li>
	<li>The n<sup>th</sup> super ugly number is guaranteed to fit in a 32-bit signed integer.</li>
</ul>

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
    
    int nthSuperUglyNumber(int n, vector<int>& primes) {
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
            } while (pq.top().val * pq.top().prime == dp[i]); // DO WHILE!

        }

        return dp[n-1];
    }
        
};
```
