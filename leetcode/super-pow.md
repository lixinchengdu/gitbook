# 372. Super Pow

* *Difficulty: Medium*

* *Topics: Math*

* *Similar Questions:*

  * [Pow(x, n)](powx-n.md)

## Problem:

<p>Your task is to calculate <i>a</i><sup><i>b</i></sup> mod 1337 where <i>a</i> is a positive integer and <i>b</i> is an extremely large positive integer given in the form of an array.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong>a = <span id="example-input-1-1">2</span>, b = <span id="example-input-1-2">[3]</span>
<strong>Output: </strong><span id="example-output-1">8</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>a = <span id="example-input-2-1">2</span>, b = <span id="example-input-2-2">[1,0]</span>
<strong>Output: </strong><span id="example-output-2">1024</span>
</pre>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    int superPow(int a, vector<int>& b) {
        int ret = 1;
        int base = a % MOD; // a need to mod first!
        for (auto it = b.rbegin(); it != b.rend(); ++it) {
            int digit = *it;
            ret = ret * pow(base, digit) % MOD;
            base = pow(base, 10);
        }
        
        return ret;
    }
    
private:
    int pow(int val, int n) {
        int ret = 1;
        int power = val;
        for (int i = 0; i < 4; ++i) {
            if ((n >> i) & 1) {
                ret = ret * power % MOD;
            }
            power = (power * power) % MOD;
        }
        
        return ret;
    }
    
    static const int MOD = 1337;
};
```
