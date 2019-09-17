# 552. Student Attendance Record II

* *Difficulty: Hard*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Student Attendance Record I](student-attendance-record-i.md)

## Problem:

<p>Given a positive integer <b>n</b>, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 10<sup>9</sup> + 7.</p>

<p>A student attendance record is a string that only contains the following three characters:</p>

<p>
<ol>
<li><b>'A'</b> : Absent. </li>
<li><b>'L'</b> : Late.</li>
<li> <b>'P'</b> : Present. </li>
</ol>
</p>

<p>
A record is regarded as rewardable if it doesn't contain <b>more than one 'A' (absent)</b> or <b>more than two continuous 'L' (late)</b>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> n = 2
<b>Output:</b> 8 
<b>Explanation:</b>
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
</pre>
</p>

<p><b>Note:</b>
The value of <b>n</b> won't exceed 100,000.
</p>



## Solutions:

```c++
class Solution {
public:
    int checkRecord(int n) {
        vector<vector<int>> dp (2, vector<int>(6, 1));
        for (int i = 1; i <= n; ++i) {
            for (int a = 0; a < 2; ++a) {
                for (int l = 0; l < 3; ++l) {
                    int pos = getPosition(a, l);
                    // get P
                    dp[i & 0x1][pos] = dp[(i-1) & 0x1][getPosition(a, 2)]; 
                    // get A
                    if (a > 0) {
                        dp[i & 0x1][pos] = (dp[i & 0x1][pos] + dp[(i-1) & 0x1][getPosition(a - 1, 2)]) % MOD;
                    }
                    // get L
                    if (l > 0) {
                        dp[i & 0x1][pos] = (dp[i & 0x1][pos] + dp[(i-1) & 0x1][getPosition(a, l - 1)]) % MOD;
                    }
                    
                }
            }
        }
        
        return dp[n & 0x1][getPosition(1, 2)];
        
    }
    
private:
    inline int getPosition(int absent, int late) {
        return absent * 3 + late;
    }
    
    static constexpr int MOD = 1000000007;
    
};
```
