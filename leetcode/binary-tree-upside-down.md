# 156. Binary Tree Upside Down

* *Difficulty: Medium*

* *Topics: Tree*

* *Similar Questions:*

  * [Reverse Linked List](reverse-linked-list.md)

## Problem:

<p>Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: </strong>[1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

<strong>Output:</strong> return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  
</pre>

<p><strong>Clarification:</strong></p>

<p>Confused what <code>[4,5,2,#,#,3,1<font face="monospace">]</font></code>&nbsp;means? Read more below on how binary tree is serialized on OJ.</p>

<p>The serialization of a binary tree follows a level order traversal, where &#39;#&#39; signifies a path terminator where no node exists below.</p>

<p>Here&#39;s an example:</p>

<pre>
   1
  / \
 2   3
    /
   4
    \
     5
</pre>

<p>The above binary tree is serialized as <code>[1,2,3,#,#,4,#,#,5]</code>.</p>

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
class Solution {
public:
    TreeNode* upsideDownBinaryTree(TreeNode* root) {
        if (root == nullptr)    return nullptr;
        if (root->left == nullptr && root->right == nullptr)    return root;
        TreeNode* leftNode = root->left;
        TreeNode* rightNode = root->right;
        TreeNode* leftSubUpsideDown = upsideDownBinaryTree(leftNode);
        TreeNode* rightSubUpsideDown = upsideDownBinaryTree(rightNode);
        
        leftNode->left = rightSubUpsideDown;
        leftNode->right = root;
        
        root->left = nullptr; // set nullptr
        root->right = nullptr; // set nullptr
        
        return leftSubUpsideDown;
    }
};
```
