# 113. Path Sum II

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Path Sum](./tests/path-sum-ii.md)

  * [Binary Tree Paths](./tests/path-sum-ii.md)

  * [Path Sum III](./tests/path-sum-ii.md)

  * [Path Sum IV](./tests/path-sum-ii.md)

## Problem:

<p>Given a binary tree and a sum, find all root-to-leaf paths where each path&#39;s sum equals the given sum.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p><strong>Example:</strong></p>

<p>Given the below binary tree and <code>sum = 22</code>,</p>

<pre>
      <strong>5</strong>
     <strong>/ \</strong>
    <strong>4   8</strong>
   <strong>/</strong>   / <strong>\</strong>
  <strong>11</strong>  13  <strong>4</strong>
 /  <strong>\</strong>    <strong>/</strong> \
7    <strong>2</strong>  <strong>5</strong>   1
</pre>

<p>Return:</p>

<pre>
[
   [5,4,11,2],
   [5,8,4,5]
]
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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector < vector<int> > ret;
        vector<int>  path;
        pathSumCore(root, sum, ret, path);
        return ret;
    }
private:
    void pathSumCore (TreeNode* root, int sum, vector < vector <int> >& ret, vector<int>& path)
    {
        if (!root)  return;
        if (!root->left && !root->right)
        {
            if (root->val == sum)
            {
                path.push_back(sum);
                ret.push_back(path);
                path.pop_back();
            }
            return;
        }
        path.push_back(root->val);
        pathSumCore(root->left, sum-root->val, ret, path);
        pathSumCore(root->right, sum-root->val, ret, path);
        path.pop_back();
    }
};
```
