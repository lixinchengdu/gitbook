# 465. Optimal Account Balancing

* *Difficulty: Hard*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as <code>[[0, 1, 10], [2, 0, 5]]</code>.</p>

<p>Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.</p>

<p><b>Note:</b>
<ol>
<li>A transaction will be given as a tuple (x, y, z). Note that <code>x &ne; y</code> and <code>z > 0</code>.</li>
<li>Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.</li>
</ol>
</p>

<p><b>Example 1:</b>
<pre>
<b>Input:</b>
[[0,1,10], [2,0,5]]

<b>Output:</b>
2

<b>Explanation:</b>
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
</pre>
</p>

<p><b>Example 2:</b>
<pre>
<b>Input:</b>
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

<b>Output:</b>
1

<b>Explanation:</b>
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    int minTransfers(vector<vector<int>>& transactions) {
        if (transactions.size() == 0)   return 0;
        unordered_map<int, int> userBalance;
        
        for (auto& transaction : transactions) {
            int sender = transaction[0];
            int receiver = transaction[1];
            int amount = transaction[2];
            
            userBalance[sender] += amount;
            userBalance[receiver] -= amount;
        }
        
        vector<int> balances;
        for (auto& entry : userBalance) {
            if (entry.second != 0)
                balances.push_back(entry.second);
        }
        
        // for (auto val : balances) {
        //     cout << val << " ";
        // }
        // cout << endl;
        
        int ret = INT_MAX;
        helper(balances, 0, ret);
        return ret;
    }
    
private:
    void helper(vector<int>& balances, int transfer, int& ret) {
    
        // cout << "s:" << transfer << endl;
        // for (auto val : balances) {
        //     cout << val << " ";
        // }
        // cout << endl;
        
        if (balances.size() <= 1) {
            ret = min(ret, transfer);
            return;
        }
        
        int amount = balances.back();
        if (amount == 0) {
            balances.pop_back();
            helper(balances, transfer, ret);
            balances.push_back(0);
            return;
        }
        for (int i = 0; i < balances.size() - 1; ++i) {
            if (amount * balances[i] < 0) {
                balances[i] += amount;
                balances.pop_back();
                helper(balances, transfer + 1, ret);
                balances.push_back(amount);
                balances[i] -= amount;
            }
        }
    }
    
};
```
