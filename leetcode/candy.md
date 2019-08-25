# 135. Candy

* *Difficulty: Hard*

* *Topics: Greedy*

* *Similar Questions:*

## Problem:

<p>There are <em>N</em> children standing in a line. Each child is assigned a rating value.</p>

<p>You are giving candies to these children subjected to the following requirements:</p>

<ul>
	<li>Each child must have at least one candy.</li>
	<li>Children with a higher rating get more candies than their neighbors.</li>
</ul>

<p>What is the minimum candies you must give?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
</pre>

## Solutions:

```c++
class Solution {
public:
    int candy(vector<int>& ratings) { // pay attention to the condition that two adjecent ratings are equal
        int n = ratings.size();
        vector<int> candyCount (n, 0);
        
        vector<pair<int, int>> ratingWithIndex;
        
        for (int i = 0; i < n; ++i) {
            ratingWithIndex.push_back({ratings[i], i});
        }
        
        sort(ratingWithIndex.begin(), ratingWithIndex.end());
        int sum = 0;
        
        for (int i = 0; i < n; ++i) {
            int index = ratingWithIndex[i].second;
            candyCount[index] = 1;
            if (index - 1 >= 0 && ratings[index] > ratings[index - 1]) {
                candyCount[index] = max(candyCount[index], candyCount[index - 1] + 1);
            }
            
            if (index + 1 < n && ratings[index] > ratings[index + 1]) {
                candyCount[index] = max(candyCount[index], candyCount[index + 1] + 1);
            }
            
            sum += candyCount[index];
        }
        
        return sum;
        
    }
};
```
