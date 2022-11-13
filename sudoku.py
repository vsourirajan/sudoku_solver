#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys
import copy
import time

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

def backtracking(board):
    """Takes a board and returns solved board."""
    def decreaseRemaining(position, remainingValues, val):
        decreased = set()
        for col in cols:
            if (position[0] + col) not in nonZeros:
                l = len(remainingValues[(position[0] + col)])
                remainingValues[(position[0] + col)].discard(val)
                if l != len(remainingValues[(position[0] + col)]):
                    decreased.add(position[0] + col)
                
            
        for row in rows:
            if (row + position[1]) not in nonZeros:
                l = len(remainingValues[row + position[1]])
                remainingValues[row + position[1]].discard(val)
                if l != len(remainingValues[row + position[1]]):
                    decreased.add(row + position[1])
            
        if(position in box1):
            for pos in box1:
                if pos not in nonZeros:
                    l = len(remainingValues[pos])
                    remainingValues[pos].discard(val)
                    if l != len(remainingValues[pos]):
                        decreased.add(pos)

        if(position in box2):
            for pos in box2:
                if pos not in nonZeros:
                    l = len(remainingValues[pos])
                    remainingValues[pos].discard(val)
                    if l != len(remainingValues[pos]):
                        decreased.add(pos)
        
        if(position in box3):
            for pos in box3:
                if pos not in nonZeros:
                    l = len(remainingValues[pos])
                    remainingValues[pos].discard(val)
                    if l != len(remainingValues[pos]):
                        decreased.add(pos)
        
        if(position in box4):
            for pos in box4:
                if pos not in nonZeros:
                    l = len(remainingValues[pos])
                    remainingValues[pos].discard(val)
                    if l != len(remainingValues[pos]):
                        decreased.add(pos)
        
        if(position in box5):
            for pos in box5:
                if pos not in nonZeros:
                    l = len(remainingValues[pos])
                    remainingValues[pos].discard(val)
                    if l != len(remainingValues[pos]):
                        decreased.add(pos)
        
        if(position in box6):
            for pos in box6:
                if pos not in nonZeros:
                    l = len(remainingValues[pos])
                    remainingValues[pos].discard(val)
                    if l != len(remainingValues[pos]):
                        decreased.add(pos)
        
        if(position in box7):
            for pos in box7:
                if pos not in nonZeros:
                    l = len(remainingValues[pos])
                    remainingValues[pos].discard(val)
                    if l != len(remainingValues[pos]):
                        decreased.add(pos)

        if(position in box8):
            for pos in box8:
                if pos not in nonZeros:
                    l = len(remainingValues[pos])
                    remainingValues[pos].discard(val)
                    if l != len(remainingValues[pos]):
                        decreased.add(pos)
        
        if(position in box9):
            for pos in box9:
                if pos not in nonZeros:
                    l = len(remainingValues[pos])
                    remainingValues[pos].discard(val)
                    if l != len(remainingValues[pos]):
                        decreased.add(pos)
        
        return decreased

    def addRemaining(position, remainingValues, val, decreased):
        for pos in decreased:
            remainingValues[pos].add(val)

    remainingValues = {}
    nonZeros = set()
    rows = ['A','B','C','D','E','F','G','H','I']
    cols = ['1','2','3','4','5','6','7','8','9']
    box1 = {"A1","A2","A3","B1","B2","B3","C1","C2","C3"}
    box2 = {"A4","A5","A6","B4","B5","B6","C4","C5","C6"}
    box3 = {"A7","A8","A9","B7","B8","B9","C7","C8","C9"}
    box4 = {"D1","D2","D3","E1","E2","E3","F1","F2","F3"}
    box5 = {"D4","D5","D6","E4","E5","E6","F4","F5","F6"}
    box6 = {"D7","D8","D9","E7","E8","E9","F7","F8","F9"}
    box7 = {"G1","G2","G3","H1","H2","H3","I1","I2","I3"}
    box8 = {"G4","G5","G6","H4","H5","H6","I4","I5","I6"}
    box9 = {"G7","G8","G9","H7","H8","H9","I7","I8","I9"}

    for position in board:
        if board[position] == 0:
            vals = {1,2,3,4,5,6,7,8,9}
            remainingValues[position] = vals
        else:
            nonZeros.add(position)
    
    for position in board:
        if board[position] != 0:
            decreaseRemaining(position, remainingValues, board[position])

    

    def helper(currboard, board, remainingValues):

        #solved board if no empty squares
        if(0 not in board.values()):
            #print_board(currboard)
            #sys.exit(0)
            return dict(currboard)
            
        #find minimum remaining value position
        minLength = 9
        minPos = None
        for position in remainingValues:
            if len(remainingValues[position]) < minLength and position not in nonZeros:
                minLength = len(remainingValues[position])
                minPos = position

        for val in remainingValues[minPos]:
            currboard[minPos] = val
            decreased = decreaseRemaining(minPos, remainingValues, val)
            nonZeros.add(minPos)
            result = helper(currboard, board, remainingValues)
            if result != False:
                return result
            nonZeros.discard(minPos)
            addRemaining(minPos, remainingValues, val, decreased)
            currboard[minPos] = 0

    
        return False

    solved_board = helper(board, board, remainingValues)
    #print(solved_board)
    return solved_board

if __name__ == '__main__':
    if len(sys.argv) > 1:
        
        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        solved_board = backtracking(board)
        
        

        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    else:
        # Running sudoku solver for boards in sudokus_start.txt $python3 sudoku.py

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        start_time  = time.time()
        times = []
        readme = open('README.txt', "a")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                      for r in range(9) for c in range(9)}

            # Print starting board. TODO: Comment this out when timing runs.
            #print_board(board)

            # Solve with backtracking
            solved_board = backtracking(board)

            # Print solved board. TODO: Comment this out when timing runs.
            #print_board(solved_board)

            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

            end_time  = time.time()
            times.append(end_time-start_time)
            #readme.write(str('%.2f'%(end_time-start_time)))
            start_time = time.time()

            

        print("Finishing all boards in file.")

        times.sort()
        readme.write(str(times[0]))
        readme.write('\n')

        readme.write(str(times[len(times) - 1]))
        readme.write('\n')

        mean = sum(times) / len(times)
        variance = sum([((x - mean) ** 2) for x in times]) / len(times)
        sd = variance ** 0.5

        readme.write(str(mean))
        readme.write('\n')

        readme.write(str(sd))
        readme.write('\n')
        
