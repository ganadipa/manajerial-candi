
from Helper import getIndex

from typing import List, Optional
matrixData = List[List[str]]

def hancurkancandi(database: List[matrixData], idCandi: str) -> None:
    data_candi = database[1]
    indexRow = getIndex(idCandi, data_candi, type='str', in_col=0)
    
    if indexRow == -1:
        print('ID Candi tidak ditemukan.')
    
    for i in range(5):
        data_candi[indexRow][i] = None

def hancurkancandi_recursion(database: List[matrixData], idCandi:str, row:Optional[int] = 0) -> None:
    data_candi = database[1]
    
    if idCandi == data_candi[row][0]:
        print(f'Apakah anda yakin ingin menghancurkan candi dengan ID {idCandi} (Y/N)? ', end = '')
        ans = input()
        
        if ans == 'Y' or ans == 'y':
            
            for i in range(5):
                data_candi[row][i] = None #MELENYAPKAN CANDI
            print()
            print('Candi telah berhasil dihancurkan.')
        
        else:
            print('input tidak jelas, dianggap tidak jadi menghancurkan candi.')
        
        return
    
    if data_candi[row][0] == '':
        print()
        print('Tidak ada candi dengan ID tersebut.')
        return
        
    
    hancurkancandi_recursion(database, idCandi, row+1)
    
    
    

    