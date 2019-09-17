# 393. UTF-8 Validation

* *Difficulty: Medium*

* *Topics: Bit Manipulation*

* *Similar Questions:*

## Problem:

<p>A character in UTF8 can be from <b>1 to 4 bytes</b> long, subjected to the following rules:</p>
<ol>
<li>For 1-byte character, the first bit is a 0, followed by its unicode code.</li>
<li>For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.</li>
</ol>
<p>This is how the UTF-8 encoding would work:</p>

<pre><code>   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
</code></pre>
<p>
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
</p>
<p>
<b>Note:</b><br />
The input is an array of integers. Only the <b>least significant 8 bits</b> of each integer is used to store the data. This means each integer represents only 1 byte of data.
</p>

<p>
<b>Example 1:</b>
<pre>
data = [197, 130, 1], which represents the octet sequence: <b>11000101 10000010 00000001</b>.

Return <b>true</b>.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
</pre>
</p>

<p>
<b>Example 2:</b>
<pre>
data = [235, 140, 4], which represented the octet sequence: <b>11101011 10001100 00000100</b>.

Return <b>false</b>.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int pos = 0;
        while (pos < data.size()) {
            bool ret = getToken(data, pos);
            //cout << pos << endl;
            if (!ret)   return false;
        }
        return true;
    }
    
private:
    bool getToken(const vector<int>& data, int& pos) {
        if (pos >= data.size()) return false;
        int firstByte = data[pos++];
        if (firstByte < 128)    return true;
        if (firstByte < 192)    return false;
        if (firstByte < 224) {
            if (pos >= data.size()) return false;
            int secondByte = data[pos++];
            return secondByte >= 128 && secondByte < 192;
        }   
        if (firstByte < 240) {
            if (pos + 1 >= data.size()) return false;
            int bytes[2];
            bytes[0] = data[pos++];
            bytes[1] = data[pos++];
            for (int i = 0 ; i < 2; ++i) {
                if (bytes[i] < 128 || bytes[i] >= 192)    return false;
            }
            
            return true;
        }
        if (firstByte < 248) {
            if (pos + 2 >= data.size()) return false;
            int bytes[3];
            bytes[0] = data[pos++];
            bytes[1] = data[pos++];
            bytes[2] = data[pos++];
            for (int i = 0 ; i < 3; ++i) {
                if (bytes[i] < 128 || bytes[i] >= 192)    return false;
            }
            return true;
        }
        
        return false;
    }
    
};
```
