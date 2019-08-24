# 297. Serialize and Deserialize Binary Tree

* *Difficulty: Hard*

* *Topics: Tree, Design*

* *Similar Questions:*

  * [Encode and Decode Strings](./tests/serialize-and-deserialize-binary-tree.md)

  * [Serialize and Deserialize BST](./tests/serialize-and-deserialize-binary-tree.md)

  * [Find Duplicate Subtrees](./tests/serialize-and-deserialize-binary-tree.md)

  * [Serialize and Deserialize N-ary Tree](./tests/serialize-and-deserialize-binary-tree.md)

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
        string res = "";
        if (!root) {res = "null";    return res;}
        //res += "[";
        res += to_string (root->val);
        res += ",";
        res += "[";
        res += serialize(root->left);
        res += "]";
        res += ",";
        res += "[";
        res += serialize(root->right);
        res += "]";
       // res += "]";
      //cout << res << endl;
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int n = data.length();
        if (n == 0) return NULL;
        if (data == "null") return NULL;
        string valStr;
        string leftStr;
        string rightStr;
        int openParCount = 0;
        int leftCommaIndex = -1;
        int rightCommaIndex = -1;
        bool findComma = false;
        for (int i = 0; i < n; i++)
        {
            switch(data[i])
            {
                case ',':   if(!findComma){leftCommaIndex = i; findComma = true;}   break;
                case '[':   openParCount ++; break;
                case ']':   if (--openParCount == 0)    {rightCommaIndex = i+1; break;}
                default:
                    ;
            }
            if (leftCommaIndex != -1 && rightCommaIndex != -1)  break;
        }
        valStr = data.substr(0, leftCommaIndex);
        leftStr = data.substr(leftCommaIndex+2, rightCommaIndex - (leftCommaIndex+2)-1);
        rightStr = data.substr(rightCommaIndex+2, n - (rightCommaIndex+2) -1);   
        //cout << valStr << endl;
        //cout << leftStr << endl;
        //cout << rightStr << endl;
        int val = stoi(valStr);
        TreeNode* res = new TreeNode(val);
        res -> left = deserialize(leftStr);
        res -> right = deserialize (rightStr);
        return res;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
```
