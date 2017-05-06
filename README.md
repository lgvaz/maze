# About
Maze generator and solver, using pygame for visualization.
Inspired by Daniel Shiffman videos on the topic:
* [Maze generator](https://www.youtube.com/watch?v=HyK_Q5rrcr4)
* [A* search](https://www.youtube.com/watch?v=aKYlikFAV4k)

# Usage
To run with default parameters, do:  
`python main.py <pathfind>`  
Where `<pathfind>` should be the name of an implemented search algorithm (a_star, depth_first).

# Options
For big mazes is better to not render interactively when building and solving, the flag `--norender` can be used to only render the final solution.  
The size of the maze can be changed using the `--num_rows=<int>` and `num_cols=<int>` options.  
For a list of all avaiable options run: `python main.py -- --help`
