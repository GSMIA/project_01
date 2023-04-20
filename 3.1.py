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

