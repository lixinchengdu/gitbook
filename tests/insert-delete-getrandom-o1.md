# 380. Insert Delete GetRandom O(1)

* *Difficulty: Medium*

* *Topics: Array, Hash Table, Design*

* *Similar Questions:*

  * [Insert Delete GetRandom O(1) - Duplicates allowed](./tests/insert-delete-getrandom-o1.md)

## Problem:

<p>Design a data structure that supports all following operations in <i>average</i> <b>O(1)</b> time.</p>

<p>
<ol>
<li><code>insert(val)</code>: Inserts an item val to the set if not already present.</li>
<li><code>remove(val)</code>: Removes an item val from the set if present.</li>
<li><code>getRandom</code>: Returns a random element from current set of elements. Each element must have the <b>same probability</b> of being returned.</li>
</ol>
</p>

<p><b>Example:</b>
<pre>
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
</pre>
</p>
## Solutions:

```c++
class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (val2pos.find(val) != val2pos.end()) return false;
        else
        {
            vals.push_back(val);
            val2pos[val] = vals.size() -1;
            return true;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (val2pos.find(val) == val2pos.end())    return false;
        else
        {
            int swapValue = vals.back();
            vals[val2pos[val]] = swapValue;
            val2pos[swapValue] = val2pos[val];
            vals.pop_back();
            val2pos.erase(val);
            return true;
        }
        
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return vals[rand()%vals.size()];
    }
    
private:
    unordered_map <int , int>   val2pos;
    vector <int> vals;
    
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```
