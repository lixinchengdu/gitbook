# 650. 2 Keys Keyboard

* *Difficulty: Medium*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [4 Keys Keyboard](4-keys-keyboard.md)

  * [Broken Calculator](broken-calculator.md)

## Problem:

<p>Initially on a notepad only one character &#39;A&#39; is present. You can perform two operations on this notepad for each step:</p>

<ol>
	<li><code>Copy All</code>: You can copy all the characters present on the notepad (partial copy is not allowed).</li>
	<li><code>Paste</code>: You can paste the characters which are copied <b>last time</b>.</li>
</ol>

<p>&nbsp;</p>

<p>Given a number <code>n</code>. You have to get <b>exactly</b> <code>n</code> &#39;A&#39; on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get <code>n</code> &#39;A&#39;.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 3
<b>Output:</b> 3
<b>Explanation:</b>
Intitally, we have one character &#39;A&#39;.
In step 1, we use <b>Copy All</b> operation.
In step 2, we use <b>Paste</b> operation to get &#39;AA&#39;.
In step 3, we use <b>Paste</b> operation to get &#39;AAA&#39;.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The <code>n</code> will be in the range [1, 1000].</li>
</ol>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    int minSteps(int n) {
        this->n = n;
        map<pair<int, int>, int> cache;
        return helper(0, n - 1, cache);
    }
    
private:
    int helper(int clipBoard, int m, map<pair<int, int>, int>& cache) {
        //cout << clipBoard << " " << m << endl;
        if (m == 0) return 0; 
        if (m < 0)  return INT_MAX;
        if (clipBoard > m)  return INT_MAX;
        
        if (cache.count({clipBoard, m})) {
            return cache[{clipBoard, m}];
        }
        
        int ret = INT_MAX;
        if (n - m != clipBoard) {
            int copyAll = helper(n - m, m, cache);
            if (copyAll < INT_MAX) {
                ret = min(ret, copyAll + 1);
            }
        }
        
        if (clipBoard != 0) {
            int reuse = helper(clipBoard, m - clipBoard, cache);
            if (reuse < INT_MAX) {
                ret = min(ret, reuse + 1);
            }
        }
        
        cache[{clipBoard, m}] = ret;
        return ret;
    }
    
    int n;
    
};
```
