#sudoku
import itertools
import sys

class Sudoku:
    def __init__(self, data):
        self.data = data

    def get_row(self, row, index_by_one=False):
        n = 1 if index_by_one else 0
        return self.data[row-n]
        
    def get_col(self, col, index_by_one=False):
        n = 1 if index_by_one else 0
        return [self.data[i][col-n] for i in range(9)]

    def get_box(self, r, c, index_by_one=False):
        n = 1 if index_by_one else 0
        return [self.data[j][i] for i in range((r-n)*3,(r-n)*3+3) for j in range((c-n)*3, (c-n)*3+3)]

    def get_cell(self, row, col, index_by_one=False):
        n = 1 if index_by_one else 0
        return self.data[row-n][col-n]

    def set_cell(self, val, row, col):
        n = 1 if index_by_one else 0
        self.data[row-n][col-n] = val

    def display(self, include_clues=False):
        print(" - - - - - - - - - - - - ")
        for i,row in enumerate(self.data):
            if include_clues:
                print ("| %s %s %s | %s %s %s | %s %s %s |"%tuple([str(x) for x in row]))
            else:
                print ("| %s %s %s | %s %s %s | %s %s %s |"%tuple([str(x) if isinstance(x, int) else " " for x in row]))
            if i==2 or i==5 or i==8:
                print(" - - - - - - - - - - - - ")

    def initialize_clues(self):
        duplicate = [row[:] for row in self.data]
        for i,row in enumerate(duplicate):
            for j,col in enumerate(row):
                if col==" ":
                    self.data[i][j]=[1,2,3,4,5,6,7,8,9]


    def solve(self):
        self.initialize_clues()
        self.solve_iterative(self.data)
        #TODO
        #recursive solution where you pass in the previous state
        #to compare to after you've tried everything. if they are the same it means
        #you've made no progress and it's unsolvable
        #also unsolvable if any of the clues sets go to empty

        #remove clues with same number in domain

    def solve_iterative(self, prev):
        #TODO
        pass



def main():
    try:
        filename = sys.argv[1]
    except:
        print("Please Include an Input File Name")
    
    with open(filename) as f:
        lines = f.readlines()

    sudoku_in = []
    for line in lines:
        sudoku_in.append([int(x) if x!=" " else " " for x in line.strip('\n').split(",")])

    sudoku = Sudoku(sudoku_in)
    sudoku.solve()
    sudoku.display(include_clues=True)

if __name__ == "__main__":
    main()