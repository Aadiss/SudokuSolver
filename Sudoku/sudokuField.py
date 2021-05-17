# tuple of all possible digits in a sigle cell
all_digits = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# tuple of tuples of tuples that contain a left upper corner coordinates and right bottom corner coordinates of each 3x3 square in matrix
# used to iterate over 3x3 matrix during alghoritm of finding possible values for each cell
square_packs = (((0, 0), (2, 2)), ((3, 0), (5, 2)), ((6, 0), (8, 2)),
                ((0, 3), (2, 5)), ((3, 3), (5, 5)), ((6, 3), (8, 5)),
                ((0, 6), (2, 8)), ((3, 6), (5, 8)), ((6, 6), (8, 8)),)


# class that represents each empty cell in a sudoku matrix, contains value, coordinates and possible values
# class has methods to find possible values, figure out in which 3x3 square it is and also to change its value
class Field:

    def __init__(self, val: int, x: int, y: int):
        self.value = val
        self.x = x
        self.y = y
        self.possibilities = []
        self.square = self.calculate_square()

    def count_possibilities(self, initial_matrix):
        """
        that method find all possible digits in a particular cell basing on a current matrix
        if no digits are found the return status is -1
        if any digits are found the possibilities attribute is equals to the list of digits
        :param initial_matrix: current matrix
        :return: -1 if failed, 1 if exists at least one possible digit
        """

        # at first all digits are possible
        final_result = list(all_digits)
        # horizontal
        for x in range(9):
            if initial_matrix[x][self.y] != 0:
                if initial_matrix[x][self.y] in final_result:
                    final_result.remove(initial_matrix[x][self.y])

        # vertical
        for y in range(9):
            if initial_matrix[self.x][y] != 0:
                if initial_matrix[self.x][y] in final_result:
                    final_result.remove(initial_matrix[self.x][y])

        # square digits
        for x in range(square_packs[self.square][0][0], square_packs[self.square][1][0] + 1):
            for y in range(square_packs[self.square][0][1], square_packs[self.square][1][1] + 1):
                if initial_matrix[x][y] != 0:
                    if initial_matrix[x][y] in final_result:
                        final_result.remove(initial_matrix[x][y])

        # after simple check in horizontal, vertical and square combination the final_result contains
        # only possible digits, if there is no digits then return -1 as a sign of fail, it means that we have to
        # modify former cells as a backtracking algorithm says
        if len(final_result) == 0:
            self.possibilities = []
            self.value = 0
            return -1
        else:
            self.possibilities = final_result
            self.value = self.possibilities[0]
            return 1

    def change_value(self):
        """
        method used to check if there are other possible digits for a particular cell than the current one
        if there are other digits the current one is removed and next one in possible list is set
        if not we have to go back to former cell in order to change value in there
        :return: -1 if there are no other digits, 1 if the value is changed
        """
        if len(self.possibilities) > 1:
            self.possibilities.remove(self.value)
            self.value = self.possibilities[0]
            return 1
        else:
            self.value = 0
            return -1

    def calculate_square(self):
        """
        method to figure out in witch of 3x3 squares the particular cell is located in
        that method is useful to find possible digits in 3x3 square, squares are numbered as follows:
        0 1 2
        3 4 5
        6 7 8
        the number corresponds index in tuple square_packs in order to know what are the borders of square
        :return:index of square as above
        """
        if self.x <= 2:
            if self.y <= 2:
                return 0

            elif self.y <= 5:
                return 3

            else:
                return 6

        elif self.x <= 5:
            if self.y <= 2:
                return 1

            elif self.y <= 5:
                return 4

            else:
                return 7

        else:
            if self.y <= 2:
                return 2

            elif self.y <= 5:
                return 5

            else:
                return 8
