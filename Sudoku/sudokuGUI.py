from tkinter import *
import numpy as np
from sudokuSolver import SudokuSolver

THEME_COLOR = "#64D638"


class GUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Simple Sudoku Solver")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.cells = []
        self.create_matrix()
        self.calculate_button = Button(text="Calculate", width=20, command=self.calculate_sudoku)
        self.calculate_button.grid(column=0, row=9, columnspan=3)
        self.reset_button = Button(text="Reset", width=20, command=self.reset_matrix)
        self.reset_button.grid(column=6, row=9, columnspan=3)

        self.window.mainloop()

    def create_matrix(self):
        """
        method to create 9x9 matrix of Entry widgets in order to put digits in them
        each Entry is saved as an object in self.cells attribute
        :return: created matrix
        """
        for x in range(9):
            for y in range(9):
                cell = Entry(self.window, width=3, borderwidth=3, font=('Ubuntu', 24))
                cell.grid(column=y, row=x, padx=1, pady=1)
                cell.insert(0, "0")

                """
                to make GUI more user friendly, bellow is format of some squares 3x3 in the matrix
                0   2
                  4 
                6   8
                mentioned above squares are highlighted in grey colour
                """
                if x <= 2:
                    if y <= 2 or y > 5:
                        cell.configure({"background": "grey"})

                elif x > 5:
                    if y <= 2 or y > 5:
                        cell.configure({"background": "grey"})

                else:
                    if 2 < y <= 5:
                        cell.configure({"background": "grey"})

                self.cells.append(cell)

    def calculate_sudoku(self):
        """
        method which is triggered with 'calculate' button, at firs it creates a numpy array basing on user input
        next step is make an object of SudokuSolver class and solve sudoku with its methods
        after finding the solution the matrix is being cleared and the solution is displayed in cells
        :return: solution
        """
        array = np.array(self.download_matrix())

        # object of SudokuSolver class and backtracking methods
        sudoku = SudokuSolver(array)
        sudoku.find_possible_values()
        sudoku.brute_force()

        # clear matrix to put solution in each cell
        self.clear_matrix()

        # fulfilling each cell with digit
        idx = 0
        for x in range(9):
            row = []
            for y in range(9):
                self.cells[idx].insert(0, str(array[x][y]))
                idx += 1

    def download_matrix(self):
        """
        method used to get user input from each cell
        :return: list of each row, ready to being put in np.array
        """
        initial_matrix = []
        idx = 0
        # iteration over rows and columns
        for x in range(9):
            row = []
            for y in range(9):
                row.append(int(self.cells[idx].get()))
                idx += 1
            initial_matrix.append(row)

        return initial_matrix

    def clear_matrix(self):
        """
        method used for clearing matrix in order to put solution in there
        :return: empty matrix
        """
        idx = 0
        for x in range(9):
            row = []
            for y in range(9):
                self.cells[idx].delete(0, "end")
                idx += 1

    def reset_matrix(self):
        """
        method used for restoring matrix to fabrice settings
        :return: empty matrix, fulfilled in 0
        """
        idx = 0
        for x in range(9):
            row = []
            for y in range(9):
                self.cells[idx].delete(0, "end")
                self.cells[idx].insert(0, "0")
                idx += 1







