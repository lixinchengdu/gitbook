# 289. Game of Life

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Set Matrix Zeroes](./tests/game-of-life.md)

## Problem:

<p>According to the <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Wikipedia&#39;s article</a>: &quot;The <b>Game of Life</b>, also known simply as <b>Life</b>, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.&quot;</p>

<p>Given a <i>board</i> with <i>m</i> by <i>n</i> cells, each cell has an initial state <i>live</i> (1) or <i>dead</i> (0). Each cell interacts with its <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" target="_blank">eight neighbors</a> (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):</p>

<ol>
	<li>Any live cell with fewer than two live neighbors dies, as if caused by under-population.</li>
	<li>Any live cell with two or three live neighbors lives on to the next generation.</li>
	<li>Any live cell with more than three live neighbors dies, as if by over-population..</li>
	<li>Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.</li>
</ol>

<p>Write a function to compute the next state (after one update) of the board given its current state.&nbsp;<span>The next state is created by applying the above rules simultaneously to every cell in the current state, where&nbsp;births and deaths occur simultaneously.</span></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: 
</strong><span id="example-input-1-1">[
&nbsp; [0,1,0],
&nbsp; [0,0,1],
&nbsp; [1,1,1],
&nbsp; [0,0,0]
]</span>
<strong>Output: 
</strong><span id="example-output-1">[
&nbsp; [0,0,0],
&nbsp; [1,0,1],
&nbsp; [0,1,1],
&nbsp; [0,1,0]
]</span>
</pre>

<p><b>Follow up</b>:</p>

<ol>
	<li>Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.</li>
	<li>In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?</li>
</ol>

## Solutions:

```c++
bool flip(int, int, vector<vector<int>>&);

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        for (int i = 0 ; i < board.size(); i++)
        {
            for (int j =0 ; j < board[0].size(); j ++)
            {
                if (flip(i,j,board))  
                {
                    v_flip.push_back(pair<int ,int>(i,j));
                   // cout << "i:"<<i << "j:" <<j << endl;
                }
            }
        }
        for (auto FlipPair: v_flip)
        {
            int left = FlipPair.first;
            int right = FlipPair.second;
            board[left][right] += 1;
            board[left][right] %= 2;
        }
        
    }
private:
    vector <pair <int, int>> v_flip;
};

bool flip(int row, int column, vector<vector<int>>& board)
{
   // cout << row << "," << column << endl;
        int LiveCounter = 0;
        for (int i = row-1; i < row+2; i++)
        {
          //  cout << "H"<<endl;
            for (int j = column-1; j < column+2; j++ )
            {
//cout << "h" << endl;
                if (i >=0 && j>= 0 && i< board.size() && j < board[0].size() && (!((i==row)&&(j==column)))&&board[i][j])
                    LiveCounter++;
            }
        }
        //cout << "cao" << endl;
        //cout << LiveCounter << endl;
        if (board[row][column])
        {
            if (LiveCounter <2 || LiveCounter > 3)  return true;
            else return false;
        }
        else
        {
            if (LiveCounter == 3)
                return true;
            else
                return false;
        }
}
```
