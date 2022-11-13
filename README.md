# Sodoku Solver with Breadth-First, Depth-First, and A-Star Search Methods

### How to Run:
bfs: breadth-first search<br />
dfs: depth-first search<br />
ast: a-star search (uses total Manhattan distance as heuristic)<br /> <br />
Run the solver as follows (python 3):<br />  `python3 sudoku.py <solving_method_abbreviated> <sudoku_board_as_a_string_with_0_spaces>`
<br /> <br />
For example: <br />
<sub><sup>`python3 sudoku.py ast 003020600900305001001806400008102900700000008006708200002609500800203009005010300`
</sup></sub>
<br />
The above command solves the board using a-star search and writes the solved board to output.txt
<br /> <br />
Runtime statistics for the 400 boards in sudokus_start.txt: <br />
        -Min: 0.0011782646179199219 seconds <br />
        -Max: 54.66166591644287 seconds <br />
        -Mean: 1.4495808857679366 seconds <br />
        -Standard Deviation: 4.474373584043112 <br />
