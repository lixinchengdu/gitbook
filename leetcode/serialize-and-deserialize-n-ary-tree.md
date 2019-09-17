# 765. Serialize and Deserialize N-ary Tree

* *Difficulty: Hard*

* *Topics: Tree*

* *Similar Questions:*

  * [Serialize and Deserialize Binary Tree](serialize-and-deserialize-binary-tree.md)

  * [Serialize and Deserialize BST](serialize-and-deserialize-bst.md)

  * [Encode N-ary Tree to Binary Tree](encode-n-ary-tree-to-binary-tree.md)

## Problem:

<p>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p>Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>

<p>For example, you may serialize the following <code>3-ary</code> tree</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<p>&nbsp;</p>

<p>as <code>[1 [3[5 6] 2 4]]</code>. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.</p>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>N</code> is in the range of <code> [1, 1000]</code></li>
	<li>Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.</li>
</ol>

## Solutions:

```c++
/*
// Definition for a Node.
class Node {
public:
    int val = NULL;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(Node* root) {
        string buf;
        serializeHelper(root, buf);
        
        return buf;
    }

    // Decodes your encoded data to tree.
    Node* deserialize(string data) {
        int pos = 0;
        return deserializeHelper(data, pos);
    }
    
private:
    Node* deserializeHelper(const string& buf, int& pos) {
        bool notNull = readBool(buf, pos);
        if (!notNull)   return nullptr;
        int val = readInt(buf, pos);
        int childrenCount = readInt(buf, pos);
        vector<Node*> children;
        for (int i = 0; i < childrenCount; ++i) {
            children.push_back(deserializeHelper(buf, pos));
        }
        Node* node = new Node(val, children);
        return node;
    }
    
    
    void serializeHelper(Node* root, string& buf) {
        if (root == nullptr) {
            writeBool(buf, false);
            return;
        }
        
        writeBool(buf, true);
        writeInt(buf, root->val);
        int childrenCount = root->children.size();
        
        writeInt(buf, childrenCount);
        for (int i = 0; i < root->children.size(); ++i) {
            serializeHelper(root->children[i], buf);
        }
    }
    
    void writeBool(string& buf, bool val) {
        buf.append(val ? "1000" : "0000"); // alignment!!!!
    }
    
    bool readBool(const string& str, int& pos) {
        char c = str[pos];
        pos += 4;
        return c == '1';
    } 
    
    void writeInt(string& str, int& val) {
        const char* valStr = reinterpret_cast<const char*> (&val);
        str.append(valStr, sizeof(val));
    }
    
    int readInt(const string& str, int& pos) {
        int val = *((reinterpret_cast<const int*> (str.data() + pos)));
        pos += sizeof(int);
        return val;
    }
    
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```
