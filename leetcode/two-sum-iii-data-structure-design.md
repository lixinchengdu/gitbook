# 170. Two Sum III - Data structure design

* *Difficulty: Easy*

* *Topics: Hash Table, Design*

* *Similar Questions:*

  * [Two Sum](two-sum.md)

  * [Unique Word Abbreviation](unique-word-abbreviation.md)

  * [Two Sum IV - Input is a BST](two-sum-iv-input-is-a-bst.md)

## Problem:

<p>Design and implement a TwoSum class. It should support the following operations: <code>add</code> and <code>find</code>.</p>

<p><code>add</code> - Add the number to an internal data structure.<br />
<code>find</code> - Find if there exists any pair of numbers which sum is equal to the value.</p>

<p><strong>Example 1:</strong></p>

<pre>
add(1); add(3); add(5);
find(4) -&gt; true
find(7) -&gt; false
</pre>

<p><strong>Example 2:</strong></p>

<pre>
add(3); add(1); add(2);
find(3) -&gt; true
find(6) -&gt; false</pre>

## Solutions:

```c++
class TwoSum {
public:
    /** Initialize your data structure here. */
    TwoSum() {
        
    }
    
    /** Add the number to an internal data structure.. */
    void add(int number) {
        ++count[number];
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        for (auto valueCount : count) {
            int target = value - valueCount.first;
            auto it = count.find(target);
            if (it != count.end() && (target != valueCount.first || it->second > 1)) return true;
        }
        return false;
    }
private:
    unordered_map<int, int> count;    
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
```
