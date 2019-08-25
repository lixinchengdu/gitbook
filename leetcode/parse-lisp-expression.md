# 736. Parse Lisp Expression

* *Difficulty: Hard*

* *Topics: String*

* *Similar Questions:*

  * [Ternary Expression Parser](ternary-expression-parser.md)

  * [Number of Atoms](number-of-atoms.md)

  * [Basic Calculator IV](basic-calculator-iv.md)

## Problem:

<p>
You are given a string <code>expression</code> representing a Lisp-like expression to return the integer value of.
</p><p>
The syntax for these expressions is given as follows.
</p><p>
<li>An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable.  Expressions always evaluate to a single integer.</li>
</p><p>
<li>(An integer could be positive or negative.)</li>
</p><p>
<li>A let-expression takes the form <code>(let v1 e1 v2 e2 ... vn en expr)</code>, where <code>let</code> is always the string <code>"let"</code>, then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable <code>v1</code> is assigned the value of the expression <code>e1</code>, the second variable <code>v2</code> is assigned the value of the expression <code>e2</code>, and so on <b>sequentially</b>; and then the value of this let-expression is the value of the expression <code>expr</code>.</li>
</p><p>
<li>An add-expression takes the form <code>(add e1 e2)</code> where <code>add</code> is always the string <code>"add"</code>, there are always two expressions <code>e1, e2</code>, and this expression evaluates to the addition of the evaluation of <code>e1</code> and the evaluation of <code>e2</code>.</li>
</p><p>
<li>A mult-expression takes the form <code>(mult e1 e2)</code> where <code>mult</code> is always the string <code>"mult"</code>, there are always two expressions <code>e1, e2</code>, and this expression evaluates to the multiplication of the evaluation of <code>e1</code> and the evaluation of <code>e2</code>.</li>
</p><p>
<li>For the purposes of this question, we will use a smaller subset of variable names.  A variable starts with a lowercase letter, then zero or more lowercase letters or digits.  Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.</li>
</p><p>
<li>Finally, there is the concept of scope.  When an expression of a variable name is evaluated, <b>within the context of that evaluation</b>, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially.  It is guaranteed that every expression is legal.  Please see the examples for more details on scope.</li>
</p>

<p><b>Evaluation Examples:</b><br />
<pre>
<b>Input:</b> (add 1 2)
<b>Output:</b> 3

<b>Input:</b> (mult 3 (add 2 3))
<b>Output:</b> 15

<b>Input:</b> (let x 2 (mult x 5))
<b>Output:</b> 10

<b>Input:</b> (let x 2 (mult x (let x 3 y 4 (add x y))))
<b>Output:</b> 14
<b>Explanation:</b> In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

<b>Input:</b> (let x 3 x 2 x)
<b>Output:</b> 2
<b>Explanation:</b> Assignment in let statements is processed sequentially.

<b>Input:</b> (let x 1 y 2 x (add x y) (add x y))
<b>Output:</b> 5
<b>Explanation:</b> The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

<b>Input:</b> (let x 2 (add (let x 3 (let x 4 x)) x))
<b>Output:</b> 6
<b>Explanation:</b> Even though (let x 4 x) has a deeper scope, it is outside the context
of the final x in the add-expression.  That final x will equal 2.

<b>Input:</b> (let a1 3 b2 (add a1 1) b2) 
<b>Output</b> 4
<b>Explanation:</b> Variable names can contain digits after the first character.

</pre>

<p><b>Note:</b>
<li>The given string <code>expression</code> is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses.  The expression is guaranteed to be legal and evaluate to an integer.</li>
<li>The length of <code>expression</code> is at most 2000.  (It is also non-empty, as that would not be a legal expression.)</li>
<li>The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.</li>
</p>
## Solutions:

```c++
class Solution {
public:
    int evaluate(string expression) {
        int pos = 0;
        unordered_map<string, int> symbols;
        return helper(expression, pos, symbols);
    }
private:
    int getNumber(string& expression, int& pos) {
        int sign = 1;
        if (expression[pos] == '-') {
            sign = -1;
            ++pos;
        }

        int val = 0;
        for (; pos < expression.length() && isdigit(expression[pos]); ++pos) {
            val = 10 * val + (expression[pos] - '0');
        }

        return sign * val;
    }

    string getOperator(string& expression, int& pos) {
        string ret;
        for (; pos < expression.length() && expression[pos] != ' '; ++pos) {
            ret.push_back(expression[pos]);
        }

        return ret;
    }

    string getSymbol(string& expression, int& pos) {
        string ret;
        for (; pos < expression.length() && expression[pos] != ' ' && expression[pos] != ')'; ++pos) {
            ret.push_back(expression[pos]);
        }

        return ret;
    }

    int helper(string& expression, int& pos, unordered_map<string, int>& symbols) {
        if (expression[pos] == '(') {
            ++pos; // remove '('
            string op = getOperator(expression, pos);
            ++pos; // remove space
            if (op != "let") {
                int oprand1 = helper(expression, pos, symbols);
                ++pos; //remove space
                int oprand2 = helper(expression, pos, symbols);
                ++pos; // remove ')'
                if (op == "add") {
                    return oprand1 + oprand2;
                } else {
                    return oprand1 * oprand2;
                }
            } else {
                unordered_set<string> add;
                unordered_map<string, int> replace;

                string symbol1 = getSymbol(expression, pos);
                ++pos; // remove space;
                if (symbols.count(symbol1) > 0) {
                    replace[symbol1] = symbols[symbol1];
                } else {
                    add.insert(symbol1);
                }
                int value1 = helper(expression, pos, symbols);
                
                ++pos; // remove space;
                symbols[symbol1] = value1;
                
                while(true) {
                    int cur = pos;
                    int val = helper(expression, pos, symbols);
                    
                    if (expression[pos] == ')') {
                        for (auto& symbol : add) {
                            symbols.erase(symbol);
                        }
                        for (auto& entry : replace) {
                            symbols[entry.first] = entry.second;
                        }
                        ++pos; // remove ')'
                        return val;
                    } else {
                        pos = cur;
                        string symbol = getSymbol(expression, pos);
                        ++pos; // remove space;
                        if (symbols.count(symbol) > 0 && add.count(symbol) == 0) {
                            replace[symbol] = symbols[symbol];
                        }

                        add.insert(symbol);
                        
                        int value = helper(expression, pos, symbols);
                        
                        ++pos; // remove space;
                        symbols[symbol] = value;
                    }
                }
            }
        } else if (expression[pos] == '-' || isdigit(expression[pos])){
            return getNumber(expression, pos);
        } else {
            string symbol = getSymbol(expression, pos);
            
            if (symbols.count(symbol) == 0) return -1;
            return symbols[symbol];
        }
    }

};
```
