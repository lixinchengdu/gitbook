# 599. Minimum Index Sum of Two Lists

* *Difficulty: Easy*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Intersection of Two Linked Lists](intersection-of-two-linked-lists.md)

## Problem:

<p>
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings. 
</p>
<p>
You need to help them find out their <b>common interest</b> with the <b>least list index sum</b>. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
<b>Output:</b> ["Shogun"]
<b>Explanation:</b> The only restaurant they both like is "Shogun".
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
<b>Output:</b> ["Shogun"]
<b>Explanation:</b> The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The length of both lists will be in the range of [1, 1000].</li>
<li>The length of strings in both lists will be in the range of [1, 30].</li>
<li>The index is starting from 0 to the list length minus 1.</li>
<li>No duplicates in both lists.</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string, int> restaurantIndex;
        for (int i = 0; i < list1.size(); ++i) {
            restaurantIndex[list1[i]] = i;
        }
        
        int minSum = INT_MAX;
        vector<string> ret;
        for (int i = 0; i < list2.size(); ++i) {
            if (restaurantIndex.count(list2[i]) > 0) {
                int index1 = restaurantIndex[list2[i]];
                if (i + index1 < minSum) {
                    minSum = i + index1;
                    ret = {list2[i]};
                } else if (i + index1 == minSum) {
                    ret.push_back(list2[i]);
                }
            }
        }
        
        return ret;
    }
};
```
