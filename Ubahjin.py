from Helper import doesUsernameExist, roleJin,  getIndex
import os
os.chdir(os.path.dirname(__file__))

from typing import List, Optional

matrixData = List[List[str]]


def ubahjin(usnJin: str, database: List[matrixData]) -> None:
    
    data_user = database[0]
    if doesUsernameExist(usnJin, in_data=data_user):
        role = ["Pengumpul", "Pembangun"][roleJin(usnJin, data_user) == 'jin_pembangun']
        antirole = ["Pembangun", "Pengumpul"][roleJin(usnJin, data_user) == 'jin_pembangun']
        
        print('Jin ini bertipe “'+role+'”. Yakin ingin mengubah ke tipe “'+antirole+'” (Y/N)? ',end ='')
        ans = input()
        
        if ans == 'Y' or ans == 'y':
            ubahjin_helper(usnJin, data_user)
            print('Jin telah berhasil diubah.')
        elif ans == 'N' or ans == 'n':
            print('Berubah pikiran? Baiklah.')
        else:
            print('Input tidak jelas, Tuan, saya asumsikan tidak jadi mengubah role jin.')
    
    else:
        print('Tidak ada jin dengan username tersebut.')
    
            

def ubahjin_helper(usnJin: str, data_user: matrixData) -> None:
    # PREKONDISI USNJIN PASTI ADA DI DALAM DATA_USER
    rowIndex = getIndex(usnJin, data_user, type = '2d', in_col = 0)
    
    role = roleJin(usnJin, data_user)
    if role == 'jin_pembangun':
        data_user[rowIndex][2] = 'jin_pengumpul'
    else:
        data_user[rowIndex][2] = 'jin_pembangun'

def ubahjin_recursion(usnJin:str, database:List[matrixData], row: Optional[int] = 0) -> None:
    if usnJin == '':
        print('Anda belum memasukkan nama jin yang ingin diubah rolenya.')
        return
    data_user = database[0]
    
    if usnJin == data_user[row][0]: #BASE CASE
        role = data_user[row][2]
        
        if role == 'jin_pembangun':
            antirole = 'jin_pengumpul'
            print('Jin ini memiliki role sebagai jin pembangun, apakah yakin ingin mengubah role jin ini menjadi')
            print('role jin pengumpul? (Y/N) ', end ='')
            
        else:
            antirole = 'jin_pembangun'
            print('Jin ini memiliki role sebagai jin pengumpul, apakah yakin ingin mengubah role jin ini menjadi')
            print('role jin pembangun? (Y/N) ', end ='')
        
        ans = input()
        
        if ans == 'Y' or ans == 'y':
            data_user[row][2] = antirole
            print('Jin telah berhasil diubah.')
        elif ans == 'N' or ans == 'n':
            print('Berubah pikiran? baiklah.')
        else:
            print('Input tidak jelas, Tuan, saya asumsikan tidak jadi mengubah role jin.')
        
        return
        
        
    
    if data_user[row][0] == '': # BASE CASE
        print('Tidak ada jin dengan username tersebut.')
        return
    
    ubahjin_recursion(usnJin, database, row+1)
