# 461. Hamming Distance

* *Difficulty: Easy*

* *Topics: Bit Manipulation*

* *Similar Questions:*

  * [Number of 1 Bits](./tests/hamming-distance.md)

  * [Total Hamming Distance](./tests/hamming-distance.md)

## Problem:

<p>The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.</p>

<p>Given two integers <code>x</code> and <code>y</code>, calculate the Hamming distance.</p>

<p><b>Note:</b><br />
0 &le; <code>x</code>, <code>y</code> &lt; 2<sup>31</sup>.
</p>

<p><b>Example:</b>
<pre>
<b>Input:</b> x = 1, y = 4

<b>Output:</b> 2

<b>Explanation:</b>
1   (0 0 0 1)
4   (0 1 0 0)
       &uarr;   &uarr;

The above arrows point to positions where the corresponding bits are different.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    int hammingDistance(int x, int y) {
        int moduloTwo = x ^ y;
        int distance = 0;
        for (int  i = 0; i < 8 * sizeof(int); i++)
        {
            distance += moduloTwo & 0x1;
            moduloTwo = moduloTwo >> 1;
        }
        return distance;
    }
};
```
