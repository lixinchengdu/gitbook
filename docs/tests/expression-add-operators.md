# 282. Expression Add Operators

* *Difficulty: Hard*

* *Topics: Divide and Conquer*

* *Similar Questions:*

  * [Evaluate Reverse Polish Notation](./tests/expression-add-operators.md)

  * [Basic Calculator](./tests/expression-add-operators.md)

  * [Basic Calculator II](./tests/expression-add-operators.md)

  * [Different Ways to Add Parentheses](./tests/expression-add-operators.md)

  * [Target Sum](./tests/expression-add-operators.md)

## Problem:

<p>Given a string that contains only digits <code>0-9</code> and a target value, return all possibilities to add <b>binary</b> operators (not unary) <code>+</code>, <code>-</code>, or <code>*</code> between the digits so they evaluate to the target value.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;123&quot;, <em>target</em> = 6
<b>Output: </b>[&quot;1+2+3&quot;, &quot;1*2*3&quot;] 
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;232&quot;, <em>target</em> = 8
<b>Output: </b>[&quot;2*3+2&quot;, &quot;2+3*2&quot;]</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;105&quot;, <em>target</em> = 5
<b>Output: </b>[&quot;1*0+5&quot;,&quot;10-5&quot;]</pre>

<p><b>Example 4:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;00&quot;, <em>target</em> = 0
<b>Output: </b>[&quot;0+0&quot;, &quot;0-0&quot;, &quot;0*0&quot;]
</pre>

<p><b>Example 5:</b></p>

<pre>
<b>Input:</b> <code><em>num</em> = </code>&quot;3456237490&quot;, <em>target</em> = 9191
<b>Output: </b>[]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector <string> result;
        string path;
        if (num.length() == 0 ) return result;
        path = string(1,num[0]);
       // cout << "path:" << path << endl;
        helper (num, 1, path, 0, 1, num[0] - '0', target, result);
        return result;
    }
    
    void helper (string& num, int k, string& path, int value, int product, long n, int target, vector<string>& result)
    {
       // cout << "path:" << path << endl;
        //cout << value << endl;
        //cout << product << endl;
        //cout << n << endl;
        if (k == num.length())
        {
            //cout << path << endl;
            //cout << value + product * n << endl;
            if (value + product * n == target) {result.push_back(path);
           // cout << path << endl;
        //    cout << value << endl;
          //  cout << product << endl;
            //cout << n << endl;
            //cout << value + product * n << endl;
            }
            return;
        }
        
        if (n != 0){
        path.append(string(1,num[k]));
        helper (num, k+1, path, value, product, n*10 + num[k]-'0', target, result);
        path.pop_back();
        }
        
        
        path.append("+" + string(1,num[k]));
        //value += product;
        //product = num[k];
        helper(num, k+1, path, value + product * n, 1, num[k]-'0', target, result);
        path.pop_back();
        path.pop_back();
        
        path.append("-" + string(1, num[k]));
        helper(num, k+1, path, value + product * n, -1, (num[k]-'0'), target, result);
        path.pop_back();
        path.pop_back();
        
        path.append("*" + string(1, num[k]));
        helper(num, k+1, path, value, product * n, num[k] - '0', target, result);
        path.pop_back();
        path.pop_back();
    }
    
};
```
