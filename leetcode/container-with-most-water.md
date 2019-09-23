# 11. Container With Most Water

* *Difficulty: Medium*

* *Topics: Array, Two Pointers*

* *Similar Questions:*

  * [Trapping Rain Water](trapping-rain-water.md)

## Problem:

<p>Given <i>n</i> non-negative integers <i>a<sub>1</sub></i>, <i>a<sub>2</sub></i>, ..., <i>a<sub>n&nbsp;</sub></i>, where each represents a point at coordinate (<i>i</i>, <i>a<sub>i</sub></i>). <i>n</i> vertical lines are drawn such that the two endpoints of line <i>i</i> is at (<i>i</i>, <i>a<sub>i</sub></i>) and (<i>i</i>, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.</p>

<p><strong>Note:&nbsp;</strong>You may not slant the container and <i>n</i> is at least 2.</p>

<p>&nbsp;</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" /></p>

<p><small>The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain&nbsp;is 49. </small></p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49</pre>

## Solutions:

```c++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int ret = 0;
        while (left < right) {
            ret = max(ret, (right - left) * min(height[left], height[right]));
            if (height[left] <= height[right]) {
                ++left;
            } else {
                --right;
            }
        }
        
        return ret;
    }
};
```

### Proof sketch
Let's `dp[i][j]` denote the optimal solution if the two axises are between `i` and `j`, inclusive. The induction then should be:

```c++
dp[i][j] = max((j - i) * min(height[i], height[j]), max(dp[i+1][j], dp[i][j-1]));
```

The only difference between `dp[i+1][j]` and `dp[i][j-1]` is the ability to use which axis as the boundary. Without losing generality, suppose `height[i] < height[j]`. If the optimal result comes from dp[i][j-1] and `ith` axis is used as the boundary. However, the result is definitely smaller than `(j - i) * min(height[i], height[j])`. 
