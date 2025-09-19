from collections import defaultdict
class Spreadsheet(object):

    def __init__(self, rows):
        self.rows = rows
        self.spreadsheet_mapper = defaultdict()


    def setCell(self, cell, value):
        self.set_cells = cell
        row , col = int(cell[1:]) , cell[0]
        self.spreadsheet_mapper[str([col  , row])] = value


    def resetCell(self, cell):
        self.set_cells = cell
        row, col = int(cell[1:]), cell[0]
        self.spreadsheet_mapper[str([col  , row])] = 0



    
    def getValue(self, formula):
        self.formula  = formula[1:]
        self.formula_array  = self.formula.split("+")
        self.lhs, self.rhs = 0, 0

        if(self.formula_array[0].isnumeric()):
            self.lhs = int(self.formula_array[0])
        else:
            left_col, left_row = self.formula_array[0][0], self.formula_array[0][1:]
            if (str([left_col, int(left_row)]) not in self.spreadsheet_mapper):
                self.lhs = 0
            else:
                self.lhs = self.spreadsheet_mapper[str([left_col , int(left_row)])]


        if(self.formula_array[1].isnumeric()):
            self.rhs =  int(self.formula_array[1])
        else:
            right_col, right_row = self.formula_array[1][0], self.formula_array[1][1:]
            if (str([right_col, int(right_row)]) not in self.spreadsheet_mapper):
                self.rhs = 0
            else:
                self.rhs = self.spreadsheet_mapper[str([right_col, int(right_row)])]
        print(self.lhs , self.rhs)
        return self.lhs+self.rhs


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)