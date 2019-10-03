# 401. Binary Watch

* *Difficulty: Easy*

* *Topics: Backtracking, Bit Manipulation*

* *Similar Questions:*

  * [Letter Combinations of a Phone Number](letter-combinations-of-a-phone-number.md)

  * [Number of 1 Bits](number-of-1-bits.md)

## Problem:

<p>A binary watch has 4 LEDs on the top which represent the <b>hours</b> (<b>0-11</b>), and the 6 LEDs on the bottom represent the <b>minutes</b> (<b>0-59</b>).</p>
<p>Each LED represents a zero or one, with the least significant bit on the right.</p>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg" height="300" />
<p>For example, the above binary watch reads "3:25".</p>

<p>Given a non-negative integer <i>n</i> which represents the number of LEDs that are currently on, return all possible times the watch could represent.</p>

<p><b>Example:</b>
<pre>Input: n = 1<br>Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]</pre>
</p>

<p><b>Note:</b><br />
<ul>
<li>The order of output does not matter.</li>
<li>The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".</li>
<li>The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".</li>
</ul>
</p>
## Solutions:

```c++
class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> ret;
        for (int i = 0; i <= num; ++i) {
            auto miniteRet = minite(i);
            auto secondRet = second(num - i);
            
            for (int j = 0 ; j < miniteRet.size(); ++j) {
                for (int k = 0; k < secondRet.size(); ++k) {
                    ret.push_back(miniteRet[j] + ":" + secondRet[k]);
                }
            }
        }
        
        return ret;
    }
private:
    vector<string> minite(int num) {
        vector<string> ret;
        for (int i = 0; i < 12; ++i) {
            if (countBit(i) == num) {
                ret.push_back(to_string(i));
            }
        }
        return ret;
    }
    
    vector<string> second(int num) {
        vector<string> ret;
        for (int i = 0; i < 60; ++i)  {
            if (countBit(i) == num) {
                if (i < 10) { 
                    ret.push_back("0" + string(1, '0' + i));
                } else {
                    ret.push_back(to_string(i));
                }
            }
        }
        
        return ret;
    }
    
    int countBit(int num) {
        int ret = 0;
        while (num > 0) {
            ++ret;
            num = num & (num - 1);
        }
        
        return ret;
    }
    
};
```

#### More concise solution

From [Huahua](https://zxi.mytechroad.com/blog/bit/leetcode-401-binary-watch/)

```c++
// Author: Huahua
// Running time: 2 ms (beats 100%)
class Solution {
public:
  vector<string> readBinaryWatch(int num) {
    vector<string> ans;
    for (int i = 0; i <= num; ++i)
      for (int h : nums(i, 12))
        for (int m : nums(num - i, 60))
          ans.push_back(to_string(h) + (m < 10 ? ":0" : ":") + to_string(m));
    return ans;
  }
private:
  // Return numbers in [0,r) that has b 1s in their binary format.
  vector<int> nums(int b, int r) {    
    vector<int> ans;
    for (int n = 0; n < r; ++n)
      if (__builtin_popcount(n) == b) ans.push_back(n);
    return ans;
  }  
};
```