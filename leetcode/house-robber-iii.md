# 337. House Robber III

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [House Robber](house-robber.md)

  * [House Robber II](house-robber-ii.md)

## Problem:

<p>The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the &quot;root.&quot; Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that &quot;all houses in this place forms a binary tree&quot;. It will automatically contact the police if two directly-linked houses were broken into on the same night.</p>

<p>Determine the maximum amount of money the thief can rob tonight without alerting the police.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input: </strong>[3,2,3,null,3,null,1]

     <font color="red">3</font>
    / \
   2   3
    \   \ 
     <font color="red">3   1
</font>
<strong>Output:</strong> 7 
<strong>Explanation:</strong>&nbsp;Maximum amount of money the thief can rob = <font color="red" style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">3</font><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> + </span><font color="red" style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">3</font><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> + </span><font color="red" style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">1</font><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> = </span><b style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">7</b><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span></pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input: </strong>[3,4,5,1,3,null,1]

&nbsp;    3
    / \
   <font color="red">4</font>   <font color="red">5</font>
  / \   \ 
 1   3   1

<strong>Output:</strong> 9
<strong>Explanation:</strong>&nbsp;Maximum amount of money the thief can rob = <font color="red">4</font> + <font color="red">5</font> = <b>9</b>.
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
    int rob(TreeNode* root) {
        return rob(root, true);
        
    }

private:
    int rob(TreeNode* root, bool couldRob) {
        if (root == nullptr)    return 0;
        if (cache.count({root, couldRob})) {
            return cache[{root, couldRob}];
        }
        
        int robRoot = 0;
        if (couldRob) {
            robRoot = root->val + rob(root->left, false) + rob(root->right, false);
        }
        
        int notRobRoot = 0;
        notRobRoot = rob(root->left, true) +  rob(root->right, true);
        
        cache[{root, couldRob}] = max(robRoot, notRobRoot);
        return max(robRoot, notRobRoot);
    }
    
    map<pair<TreeNode*, bool>, int> cache;
    
};
```
