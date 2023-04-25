from typing import Any
class Matrix: 
 
    def __init__(self, dims, fill:Any=0):    
     self.rows = dims[0]  
     self.cols = dims[1]   
     self.A = [[fill] * self.cols for _ in range(self.rows)]

    def __str__(self): 
    
        m = len(self.A) # Get the first dimension 
    
        mtxStr = ''
        mtxStr += '------------- output -------------\n'     
            
        for i in range(m):
                
            mtxStr += ('|' + ', '.join( map(lambda x:'{0:8.3f}'.format(x), self.A[i])) + '| \n')
        mtxStr += '----------------------------------'
        return mtxStr  
        
    def rowcol(self):
        return self.cols, self.rows
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            i = key[0]
            j = key[1]
            self.A[i][j] = value
    
    def fill_matrix(self, fill_list):
        index = 0
        for i in range(self.rows):
            try:
                for j in range(self.cols):
                    self.A[i][j] = fill_list[index]
                    index += 1
            except IndexError:
                print (f"Matrix not filled \nMatrix fill stopped at: row {i}, Column {j}")
             
                break        
        return fill_list[index:]
a=Matrix([5, 7])
a[1,4] = -10
print(a)
overflow = a.fill_matrix([_ for _ in range(50)])
print(a)
print('Количество колонок', a.rowcol()[0], 'Количество строк', a.rowcol()[1])

# Да, хороший вариант.
# Также есть дополнительный вариант через словари

class Table:
    def __init__(self, colnames: list):
        self.colnames = colnames
        self.rows = []

    def add_row(self, row: dict):
        if any(colname not in tuple(row) for colname in self.colnames):  # хотя бы один элемент не соответствует
            print('Такой колонки нет')
        else:
            self.rows.append(row)

    def get_column(self, colname):
        if (colname not in self.colnames):
            print('Такой колонки нет')
        return [r[colname] for r in self.rows]


    def sum(self, colname: str):
        if colname not in self.colnames:
          print('Неправильный формат')
        return sum([r[colname] for r in self.rows])



table1 = Table([1, 2])
table1.add_row({1: 10, 2: 20})
table1.add_row({1: 20, 2: 400})
table1.add_row({1: 30, 2: 600})
table1.add_row({1: 40, 2: 800})
print(table1.get_column(1))
print(table1.get_column(2))
print(table1.rows)
