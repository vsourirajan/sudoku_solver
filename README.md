# Sudoku Solver

### Methodology
The solver utilizes backtracking to explore possible solutions. Additionally, I have implemented minimum remaining values heuristic 
and forward checking to reduce the size of the search space and optimize runtime.

### How to Run:
Run the solver as follows (python 3):<br />  `python3 sudoku.py <sudoku_board_as_a_string_with_no_spaces>`
<br /> <br />
For example:<br /> 
<sub>`python3 sudoku.py 003020600900305001001806400008102900700000008006708200002609500800203009005010300`</sub>
<br /><br />
The above command solves the board (assuming the 0s as empty spaces) and writes the solved board to output.txt
<br /> <br />
Runtime statistics for the 400 boards in sudokus_start.txt: <br />
        -Min Solve Time: 0.001 seconds <br />
        -Max Solve Time: 54.662 seconds <br />
        -Mean Solve Time: 1.449 seconds <br />
        -Standard Deviation: 4.474 
