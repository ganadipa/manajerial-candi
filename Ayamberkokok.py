
from Helper import countData
from typing import List, Optional
matrixData = List[List[str]]

def ayamberkokok(database: List[matrixData]) -> bool:
    data_candi = database[1]
    jumlahCandi = countData(data_candi)
    print(f'Jumlah Candi: {countData(data_candi)}')
    print()
    if jumlahCandi < 100:
        return False
    else:
        return True

def ayamberkokok_recursion(database: List[matrixData], row:Optional[int] = 0, countNone:Optional[int] = 0) -> bool:
    data_candi = database[1]
    jumlahCandi = row -1 -countNone
    
    if data_candi[row][0] == '': # BASE CASE
        print(f'Jumlah Candi: {jumlahCandi}')
        print()
        if jumlahCandi < 100:
            return True
        else:
            return False
        
    if data_candi[row][0] == None:
        return ayamberkokok_recursion(database, row+1, countNone+1)
    
    return ayamberkokok_recursion(database, row + 1, countNone)
    
    
        