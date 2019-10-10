# 1307. Ugly Number III

* *Difficulty: Medium*

* *Topics: Math, Binary Search*

* *Similar Questions:*

  * [Ugly Number II](ugly-number-ii.md)

## Problem:

<p>Write a program to find the&nbsp;<code>n</code>-th ugly number.</p>

<p>Ugly numbers are<strong>&nbsp;positive integers</strong>&nbsp;which are divisible by&nbsp;<code>a</code>&nbsp;<strong>or</strong>&nbsp;<code>b</code>&nbsp;<strong>or</strong> <code>c</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, a = 2, b = 3, c = 5
<strong>Output:</strong> 4
<strong>Explanation: </strong>The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4, a = 2, b = 3, c = 4
<strong>Output:</strong> 6
<strong>Explanation: </strong>The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 5, a = 2, b = 11, c = 13
<strong>Output:</strong> 10
<strong>Explanation: </strong>The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> n = 1000000000, a = 2, b = 217983653, c = 336916467
<strong>Output:</strong> 1999999984
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, a, b, c &lt;= 10^9</code></li>
	<li><code>1 &lt;= a * b * c &lt;= 10^18</code></li>
	<li>It&#39;s guaranteed that the result will be in range&nbsp;<code>[1,&nbsp;2 * 10^9]</code></li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int nthUglyNumber(int n, int A, int B, int C) {
        int left = 1;
        int right = INT_MAX;
        
        long a = A;
        long b = B;
        long c = C;
        
        long d = gcm(a, b);
         
        long e = gcm(a, c);
        e = min(e, long(INT_MAX) );
        long f = gcm(b, c);
        f = min(f, long(INT_MAX) );
        
        long g = gcm(e, f);
    
        g = min(g, long(INT_MAX) );
    
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (countUglyNumber(mid, a, b, c, d, e, f, g) >= n) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
private:
    int countUglyNumber(long num, long a, long b, long c, long d, long e, long f, long g) {
        return  num / a + num / b + num / c - num / d - num / e - num / f + num / g;
    }
    
    int gcd(int x, int y) {
        if (y > x) {
            return gcd(y, x);
        }
        
        if (y == 0) return x;
        return gcd(y, x % y);
    }
    
    long gcm(long x, long y) {
        return (x * y) / gcd(x, y);
    }
    
};

```
