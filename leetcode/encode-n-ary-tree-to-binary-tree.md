# 771. Encode N-ary Tree to Binary Tree

* *Difficulty: Hard*

* *Topics: Tree*

* *Similar Questions:*

  * [Serialize and Deserialize N-ary Tree](serialize-and-deserialize-n-ary-tree.md)

## Problem:

<p>Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.</p>

<p>For example, you may encode the following <code>3-ary</code> tree to a binary tree in this way:</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreebinarytreeexample.png" style="width: 100%; max-width: 640px" /></p>

<p>&nbsp;</p>

<p>Note that the above is just an example which <em>might or might not</em> work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.</p>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>N</code> is in the range of <code> [1, 1000]</code></li>
	<li>Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.</li>
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

    // Encodes an n-ary tree to a binary tree.
    TreeNode* encode(Node* root) {
        if (root == nullptr)    return nullptr;
        int val = root->val;
        TreeNode* treeRoot = new TreeNode(val);
        if (root->children.empty()) return treeRoot;
        treeRoot->left = encode(root->children[0]);
        TreeNode* cur = treeRoot->left;
        for (int i = 1; i < root->children.size(); ++i) {
            cur->right = encode(root->children[i]);
            cur = cur->right;
        }
        
        return treeRoot;
    }

    // Decodes your binary tree to an n-ary tree.
    Node* decode(TreeNode* root) {
        if (root == nullptr)    return nullptr;
        Node* nAryTreeRoot = new Node();
        nAryTreeRoot->val = root->val;
        TreeNode* cur = root->left;
        while (cur != nullptr) {
            nAryTreeRoot->children.push_back(decode(cur));
            cur = cur->right;
        }
        return nAryTreeRoot;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(root));
```
