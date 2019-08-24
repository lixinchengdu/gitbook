# 257. Binary Tree Paths

* *Difficulty: Easy*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Path Sum II](./tests/binary-tree-paths.md)

  * [Smallest String Starting From Leaf](./tests/binary-tree-paths.md)

## Problem:

<p>Given a binary tree, return all root-to-leaf paths.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>

   1
 /   \
2     3
 \
  5

<strong>Output:</strong> [&quot;1-&gt;2-&gt;5&quot;, &quot;1-&gt;3&quot;]

<strong>Explanation:</strong> All root-to-leaf paths are: 1-&gt;2-&gt;5, 1-&gt;3
</pre>
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
    vector<string> res;
    vector<string> binaryTreePaths(TreeNode* root) {
        if (!root)  return res;
        helper (root, "");
        return res;
    }
    void helper (TreeNode* root, string path)
    {
        //cout << path.substr(2) << endl;
        if (root -> left == NULL && root->right == NULL)  {res.push_back((path + "->"+ to_string(root->val)).substr(2));}
        if (root -> left) helper (root->left, path + "->" + to_string(root->val));
        if (root -> right) helper (root->right, path + "->"+ to_string(root->val));
    }
};
```
