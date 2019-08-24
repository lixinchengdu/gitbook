# 372. Super Pow

* *Difficulty: Medium*

* *Topics: Math*

* *Similar Questions:*

  * [Pow(x, n)](./tests/super-pow.md)

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
        if (b.size() == 0)  return 0;
        return superPowHelper (a, b, b.size() - 1);
    }

private:
    int modulo = 1337;
    int superPowHelper (int a, vector<int>&b, int end)
    {    //cout << b[b.size()-1] << endl;
        // cout << end << endl;
        if (end == 0)  { return powResursive(a, b[0], modulo);}
        return powResursive(superPowHelper(a, b, end-1), 10, modulo) * powResursive(a, b[end], modulo)%modulo; 
    }
    
    int powResursive(int base, int power, int modulo)
    {
        if (power == 0) return 1;
        if (power == 1) return base%modulo;
        //cout << "rec" << endl;
        //cout << powResursive(base, power/2, modulo)*powResursive(base,(power+1)/2, modulo) << endl;
        //int result = 
        return powResursive(base, power/2, modulo)*powResursive(base,(power+1)/2, modulo)%modulo;
    }

};
```
