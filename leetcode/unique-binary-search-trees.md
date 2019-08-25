# 96. Unique Binary Search Trees

* *Difficulty: Medium*

* *Topics: Dynamic Programming, Tree*

* *Similar Questions:*

  * [Unique Binary Search Trees II](unique-binary-search-trees-ii.md)

## Problem:

<p>Given <em>n</em>, how many structurally unique <strong>BST&#39;s</strong> (binary search trees) that store values 1 ...&nbsp;<em>n</em>?</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong> 5
<strong>Explanation:
</strong>Given <em>n</em> = 3, there are a total of 5 unique BST&#39;s:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
</pre>

## Solutions:

```c++
class Solution {
public:
    int numTrees(int n) {
        map<pair<int, int>, int> cache;
        return helper(1, n, cache);
    }
    
    int helper(int left, int right, map<pair<int, int>, int>& cache) {
        if (left > right)   return 1; // return 1!
        if (left == right)  return 1;
        auto range = make_pair(left, right);
        if (cache.count(range) != 0)    return cache[range];
        int count = 0;
        for (int num = left; num <= right; ++num) {
            count += helper(left, num - 1, cache) * helper(num + 1, right, cache);
        }
        
        cache[range] = count;
        return count;
    }
};
```
