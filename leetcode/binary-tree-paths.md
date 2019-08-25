# 257. Binary Tree Paths

* *Difficulty: Easy*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Path Sum II](path-sum-ii.md)

  * [Smallest String Starting From Leaf](smallest-string-starting-from-leaf.md)

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
    vector<string> binaryTreePaths(TreeNode* root) {
        if (root == NULL)   return {};
        vector<vector<int>> ret;
        vector<int> path;
        helper(root, path, ret);
        vector<string> strRet;
        for (auto& intPath : ret) {
            strRet.push_back(join(intPath));
        }
        
        return strRet;
    }
    
    void helper(TreeNode* root, vector<int>& path, vector<vector<int>>& ret) {
        path.push_back(root->val);
        if (root->left == NULL && root->right == NULL) {
            ret.push_back(path);
            path.pop_back();
            return;
        }
        
        if (root->left) helper(root->left, path, ret);
        if (root->right) helper(root->right, path, ret);
        path.pop_back();
    }
    
    string join(vector<int>& nums) {
        stringstream ss;
        for (int i = 0; i < nums.size(); ++i) {
            if (i != 0) {
                ss << "->";
            }
            ss << nums[i];
        }
        
        return ss.str();
    }
};
```
