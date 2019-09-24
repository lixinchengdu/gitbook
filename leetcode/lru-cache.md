# 146. LRU Cache

* *Difficulty: Medium*

* *Topics: Design*

* *Similar Questions:*

  * [LFU Cache](lfu-cache.md)

  * [Design In-Memory File System](design-in-memory-file-system.md)

  * [Design Compressed String Iterator](design-compressed-string-iterator.md)

## Problem:

<p>Design and implement a data structure for <a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a>. It should support the following operations: <code>get</code> and <code>put</code>.</p>

<p><code>get(key)</code> - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.<br />
<code>put(key, value)</code> - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.</p>

<p>The cache is initialized with a <strong>positive</strong> capacity.</p>

<p><b>Follow up:</b><br />
Could you do both operations in <b>O(1)</b> time complexity?</p>

<p><b>Example:</b></p>

<pre>
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class LRUCache {
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if (keyToNode.count(key) == 0) {
            return -1;
        }
        
        int val = keyToNode[key]->second;
        cache.splice(cache.begin(), cache, keyToNode[key]);
        return val;
    }
    
    void put(int key, int value) {
        if (keyToNode.count(key) > 0) {
            cache.splice(cache.begin(), cache, keyToNode[key]);
            keyToNode[key]->second = value;
            return;
        }
        
        cache.insert(cache.begin(), {key, value});
        keyToNode[key] = cache.begin();
        
        if (cache.size() > capacity) {
            int key = cache.back().first;
            cache.pop_back();
            keyToNode.erase(key);
        }
    }
private:
    int capacity;
    list<pair<int, int>> cache;
    unordered_map<int, list<pair<int, int>>::iterator> keyToNode;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```
