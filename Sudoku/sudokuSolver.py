from sudokuField import Field


class SudokuSolver:

    def __init__(self, initial_matrix):
        self.initial_matrix = initial_matrix
        self.list_of_field_classes = []
        self.make_list_of_empty_fields()
        self.index = 0
        self.solved = False

    def make_list_of_empty_fields(self):
        """
        method iterate over entire user input and find out which cell are empty
        of course empty means there are equals to 0, if cell is empty then new object of
        Field class is created and appended to list of empty cells
        Field has value equals to 0, and x, y coordinates basing on its location in matrix
        :return: list of empty cells
        """
        for x in range(9):
            for y in range(9):
                if self.initial_matrix[x][y] == 0:
                    new_empty_field = Field(self.initial_matrix[x][y], x, y)
                    self.list_of_field_classes.append(new_empty_field)

    def find_possible_values(self):
        """
        first step in order to find the solution, for each empty cell calculate possible digits and if there is only one
        possible digit the value of cell is set and that cell is removed from empty ones, it happens because of the fact
        if we have only one possibility we have to use it
        it is a way of optimization of backtracking algorithm, we do not care about cells which are obvious
        :return: possibly modified matrix
        """
        for field in self.list_of_field_classes:
            field.count_possibilities(self.initial_matrix)
            if len(field.possibilities) == 1:
                x_cor = field.x
                y_cor = field.y
                self.initial_matrix[x_cor][y_cor] = field.value
                self.list_of_field_classes.remove(field)

    def brute_force(self):
        """
        main algorithm, while loop works until solution is found
        at first we know we are in first empty cell, we set a value and go ahead
        in opposite case we check the status, which says whether there is a possible digit to put in a cell or not
        status is returned as a result of count_possibilities method from Field class basing on updated matrix
        if there are no possibilities we have to trace back to the former cell and change value in there
        :return: solved problem
        """
        while self.solved is False:

            if self.index == 0:
                x_cor = self.list_of_field_classes[0].x
                y_cor = self.list_of_field_classes[0].y
                self.initial_matrix[x_cor][y_cor] = self.list_of_field_classes[0].value
                self.index += 1

            else:
                status = self.list_of_field_classes[self.index].count_possibilities(self.initial_matrix)

                if status == -1:
                    """
                    the most complex part of algorithm because if status equals to -1 we have to find one of former cells 
                    which has another possible digit to set up, another while loop deeps into former cells and check if
                    cell has another digit, if not deep again and again until find the cell with another possibility 
                    """
                    x_cor = self.list_of_field_classes[self.index].x
                    y_cor = self.list_of_field_classes[self.index].y
                    self.initial_matrix[x_cor][y_cor] = 0
                    self.index -= 1

                    while self.list_of_field_classes[self.index].change_value() == -1:
                        # if there is no possible digit we set current cell location as 0 in matrix and deep again
                        x_cor = self.list_of_field_classes[self.index].x
                        y_cor = self.list_of_field_classes[self.index].y
                        self.initial_matrix[x_cor][y_cor] = 0
                        self.index -= 1

                    x_cor = self.list_of_field_classes[self.index].x
                    y_cor = self.list_of_field_classes[self.index].y
                    self.initial_matrix[x_cor][y_cor] = self.list_of_field_classes[self.index].value
                    self.index += 1

                else:
                    x_cor = self.list_of_field_classes[self.index].x
                    y_cor = self.list_of_field_classes[self.index].y
                    self.initial_matrix[x_cor][y_cor] = self.list_of_field_classes[self.index].value
                    self.index += 1

                    if self.index >= len(self.list_of_field_classes):
                        self.solved = True


