# 297. Serialize and Deserialize Binary Tree

* *Difficulty: Hard*

* *Topics: Tree, Design*

* *Similar Questions:*

  * [Encode and Decode Strings](encode-and-decode-strings.md)

  * [Serialize and Deserialize BST](serialize-and-deserialize-bst.md)

  * [Find Duplicate Subtrees](find-duplicate-subtrees.md)

  * [Serialize and Deserialize N-ary Tree](serialize-and-deserialize-n-ary-tree.md)

## Problem:

<p>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p>Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>

<p><strong>Example:&nbsp;</strong></p>

<pre>
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as <code>&quot;[1,2,3,null,null,4,5]&quot;</code>
</pre>

<p><strong>Clarification:</strong> The above format is the same as <a href="/faq/#binary-tree">how LeetCode serializes a binary tree</a>. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.</p>

<p><strong>Note:&nbsp;</strong>Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.</p>

## Solutions:

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string ret;
        serializeHelper(root, ret);
        return ret;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int pos = 0;
        return deserializeHelper(data, pos);
    }
    
private:
    void serializeHelper(TreeNode* root, string& ret) {
        const static string NULL_STRING = "NULL"; 
        if (root == nullptr) {
            ret.append(NULL_STRING);
            ret.push_back(' ');
            return;
        }
        
        ret.append(to_string(root->val));
        ret.push_back(' ');
        serializeHelper(root->left, ret);
        serializeHelper(root->right, ret);
    }
    
    TreeNode* deserializeHelper(string& data, int& pos) {
        string token = getToken(data, pos);
        if (token == "NULL") {
            return nullptr;
        }
        
        TreeNode* root = new TreeNode(stoi(token));
        root->left = deserializeHelper(data, pos);
        root->right = deserializeHelper(data, pos);
        return root;
    }
    
    string getToken(string& data, int& pos) {
        string ret;
        for (;data[pos] != ' '; ++pos) {
            ret.push_back(data[pos]);
        }
        
        ++pos; // remove space
        return ret;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root)); 
```
