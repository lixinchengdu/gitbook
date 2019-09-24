# 655. Print Binary Tree

* *Difficulty: Medium*

* *Topics: Tree*

* *Similar Questions:*

## Problem:

<p>Print a binary tree in an m*n 2D string array following these rules: </p>

<ol>
<li>The row number <code>m</code> should be equal to the height of the given binary tree.</li>
<li>The column number <code>n</code> should always be an odd number.</li>
<li>The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (<b>left-bottom part and right-bottom part</b>). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them. </li>
<li>Each unused space should contain an empty string <code>""</code>.</li>
<li>Print the subtrees following the same rules.</li>
</ol>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
     1
    /
   2
<b>Output:</b>
[["", "1", ""],
 ["2", "", ""]]
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>
     1
    / \
   2   3
    \
     4
<b>Output:</b>
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b>
      1
     / \
    2   5
   / 
  3 
 / 
4 
<b>Output:</b>

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
</pre>
</p>

<p><b>Note:</b>
The height of binary tree is in the range of [1, 10].
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
    vector<vector<string>> printTree(TreeNode* root) {
        if (root == nullptr)    return {};
        int height = getHeight(root);
        vector<vector<string>> ret (height, vector<string>((1 << height) - 1, ""));
        
        printHelper(root, 0, 0, (1 << height) - 2, ret);
        return ret;
    }
    
private:
    int getHeight(TreeNode* root) {
        if (root == nullptr)    return 0;
        return 1 + max(getHeight(root->left), getHeight(root->right));
    }
    
    void printHelper(TreeNode* root, int level, int left, int right, vector<vector<string>>& ret) {
        if (root == nullptr)    return;
        int mid = left + (right - left) / 2;
        ret[level][mid] = to_string(root->val);
        printHelper(root->left, level + 1, left, mid - 1, ret);
        printHelper(root->right, level + 1, mid + 1, right, ret);
    }
    
};
```
