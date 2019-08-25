# 271. Encode and Decode Strings

* *Difficulty: Medium*

* *Topics: String*

* *Similar Questions:*

  * [Count and Say](count-and-say.md)

  * [Serialize and Deserialize Binary Tree](serialize-and-deserialize-binary-tree.md)

  * [String Compression](string-compression.md)

  * [Count Binary Substrings](count-binary-substrings.md)

## Problem:

<p>Design an algorithm to encode <b>a list of strings</b> to <b>a string</b>. The encoded string is then sent over the network and is decoded back to the original list of strings.</p>

<p>Machine 1 (sender) has the function:</p>

<pre>
string encode(vector&lt;string&gt; strs) {
  // ... your code
  return encoded_string;
}</pre>
Machine 2 (receiver) has the function:

<pre>
vector&lt;string&gt; decode(string s) {
  //... your code
  return strs;
}
</pre>

<p>So Machine 1 does:</p>

<pre>
string encoded_string = encode(strs);
</pre>

<p>and Machine 2 does:</p>

<pre>
vector&lt;string&gt; strs2 = decode(encoded_string);
</pre>

<p><code>strs2</code> in Machine 2 should be the same as <code>strs</code> in Machine 1.</p>

<p>Implement the <code>encode</code> and <code>decode</code> methods.</p>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li>The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.</li>
	<li>Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.</li>
	<li>Do not rely on any library method such as <code>eval</code> or serialize methods. You should implement your own encode/decode algorithm.</li>
</ul>

## Solutions:

```c++
class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string serial;
        int n = strs.size();
        serial.append(writeInt(n));
        
        for (int i = 0; i < n; ++i) {
            serial.append(writeString(strs[i]));
        }
        return serial;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> strs;
        const char* buf = s.c_str();
        int n = readInt(buf);
        for (int i = 0; i < n; ++i) {
            strs.push_back(readString(buf));
        }
        return strs;
    }

    static const int INT_SIZE = 4;

    string writeString(string str) {
        int strLen = str.length();
        string serial;
        serial.append(writeInt(strLen));
        char* buf = new char[strLen];
        memcpy(buf, str.c_str(), strLen);
        serial.append(string(buf, strLen));
        delete[] buf;
        return serial;
    }

    string readString(const char*& buf) {
        int strLen = readInt(buf);
        string content(buf, strLen);
        buf += strLen;
        return content;
    }

    string writeInt(int num) {
        char buf[INT_SIZE];
        memcpy(buf, (void*)(&num), INT_SIZE);
        return string(buf, INT_SIZE);
    }   

    int readInt(const char*& buf) {
        int num = 0;
        memcpy((void*)(&num), buf, INT_SIZE);
        buf += INT_SIZE;
        return num;
    } 
};
```
