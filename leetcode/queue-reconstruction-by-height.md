# 406. Queue Reconstruction by Height

* *Difficulty: Medium*

* *Topics: Greedy*

* *Similar Questions:*

  * [Count of Smaller Numbers After Self](count-of-smaller-numbers-after-self.md)

## Problem:

<p>Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers <code>(h, k)</code>, where <code>h</code> is the height of the person and <code>k</code> is the number of people in front of this person who have a height greater than or equal to <code>h</code>. Write an algorithm to reconstruct the queue.</p>

<p><b>Note:</b><br />
The number of people is less than 1,100.</p>
&nbsp;

<p><b>Example</b></p>

<pre>
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        auto comparator = [](const vector<int>& person1, const vector<int>& person2) {
            return person1[0] == person2[0] ? person1[1] < person2[1] : person1[0] > person2[0];  
        };
        
        sort(people.begin(), people.end(), comparator);
        
        vector<vector<int>> ret;
        
        for (auto& person : people) {
            ret.insert(ret.begin() + person[1], person);
        }
        
        return ret;
    }
};
```
