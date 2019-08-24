# 450. Delete Node in a BST

* *Difficulty: Medium*

* *Topics: Tree*

* *Similar Questions:*

  * [Split BST](./tests/delete-node-in-a-bst.md)

## Problem:

<p>Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.</p>

<p>Basically, the deletion can be divided into two stages:
<ol>
<li>Search for a node to remove.</li>
<li>If the node is found, delete the node.</li>
</ol>
</p>

<p><b>Note:</b> Time complexity should be O(height of tree).</p>

<p><b>Example:</b>
<pre>
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
</pre>
</p>
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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root)  return NULL;
        //cout << root -> val << endl;
        if (root-> val == key) 
        {
            if (!root->left)
            {
                delete root;
                return root->right;
            }
            if (!root->right)
            {
                delete root;
                return root->left;
            }
           // TreeNode* parentNode = root;
            TreeNode* curNode = root->right;
            while (curNode->left)   {curNode = curNode->left;}
            root->val = curNode->val;
            root->right = deleteNode(root->right, curNode->val);
            //delete curNode;
           // if (parentNode == root) parentNode -> right = NULL;
           // else parentNode -> left = NULL;
            //parentNode -> left = NULL;
           // cout << "aha2!" << endl;
            return root;
        }
        if (key < root-> val) {root->left = deleteNode(root->left, key);}
        else root->right = deleteNode (root->right, key);
        //cout << "aha!" << endl;
       // cout << root -> val << endl;
        return root;
    }
};
```
