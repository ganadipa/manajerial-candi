import os
os.chdir(os.path.dirname(__file__))
from typing import List
from Helper import getIndex, appendData, countData,doesUsernameExist
matrixData = List[List[str]]

def meditasi(database: List[matrixData]) -> None:
    data_user = database[0]
    status_info = database[3][1]
    rowIndex = getIndex('bandung_bondowoso', array=data_user, type = '2d', in_col = 2)
    
    data_user[rowIndex][2] = 'bandung_bondowoso_enlightened'
    status_info[2] = 'bandung_bondowoso_enlightened'

def undo(database: List[matrixData]) -> None:
    stack = database[4]
    jumlahStack = countData(stack)
    if jumlahStack == 0:
        print('Tidak ada record hapusjin yang dapat di undo.')
        return
    data_user = database[0]
    data_candi = database[1]
    rowIndex = getIndex('', stack, type = '2d', in_col = 0) - 1
    usn = stack[rowIndex][0]
    while True:
        dataPerRow = stack[rowIndex]
        
        if dataPerRow[0] != usn:
            break
        
        if not(doesUsernameExist(dataPerRow[0], in_data=data_user, role = 'jin')):
            user_datum = [dataPerRow[0], dataPerRow[1], dataPerRow[2]]
            appendData(data_user, user_datum) ##### MASIH NGACO
        
        id1 = getIndex(None, data_candi, type='2d', in_col = 0)
        id2 = getIndex('', data_candi, type='2d', in_col=0)
        if id1 < id2:
            idCandi = id1
        else:
            idCandi = id2
        candi_datum = [idCandi, dataPerRow[4], dataPerRow[5], dataPerRow[6], dataPerRow[7]]
        appendData(data_candi, candi_datum)
        
        
        stack[rowIndex] = ['' for i in range(10)]
        rowIndex -= 1
    
    print('Undo telah dilaksanakan.')
    
    
        
