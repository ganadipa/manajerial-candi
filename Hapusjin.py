from Helper import countJin, doesUsernameExist, append, appendData
from typing import List

matrixData = List[List[str]]

def hapusjin(database: List[matrixData]) -> None:
    data_user = database[0]
    data_candi = database[1]
    trashcan_stack = database[4]
    
    if countJin(data_user) == 0:
        print('Bandung belum memiliki jin sama sekali !')
        return
    else:
        print("Masukkan username jin: ", end = '')
        usnJin = input()
        if not(doesUsernameExist(usnJin, in_data=data_user, role = 'jin')):
            print('Tidak ada jin dengan username tersebut.')
        else:
            print('Apakah Anda yakin ingin menghapus jin dengan username', usnJin, '(Y/N)? ', end = '')
            ans = input()
            
            if ans == 'Y' or ans == 'y':
                hapusJin_helper(usnJin, data_user, data_candi, trashcan_stack)
                print('jin telah berhasil dihapus dari alam gaib.')
                
            elif ans == 'N' or ans == 'n':
                print('Hahaha, hanya bercanda ya... Saya kira tuan Bondowoso serius ingin menghapus jin', usnJin)
                
            
def hapusJin_helper(usn: str, data_user: matrixData, data_candi: matrixData, trashcan_stack: matrixData) -> None:
    #PREKONDISI: USN SUDAH PASTI ADA DI DALAM MATRIKS DATA_USER
    users_row = 0
    while True:
        check_usn = data_user[users_row][0]
        if usn == check_usn:
            break
        users_row += 1

    

    
    if doesUsernameExist(usn, in_data = data_candi):
        # JIKA ADA KITA AMBIL ADA DI BARIS BERAPA SAJA.
        iterator = 0 
        
        while True:
            check_usn = data_candi[iterator][1]
            if check_usn == '':
                break
            
            
            
            if usn ==check_usn:
                data_candi_with_builder = ['' for i in range(10)]
                data_candi_with_builder[0] = usn
                data_candi_with_builder[1] = data_user[users_row][1]
                data_candi_with_builder[2] = data_user[users_row][2]
                append(data_candi_with_builder, data_candi[iterator])
                appendData(trashcan_stack, data_candi_with_builder)
                
                
                data_candi[iterator][0] = None
                data_candi[iterator][1] = None
                data_candi[iterator][2] = None
                data_candi[iterator][3] = None
                data_candi[iterator][4] = None 
            iterator += 1
    
    else:
        data_candi_with_builder = ['' for i in range(10)]
        data_candi_with_builder[0] = usn
        data_candi_with_builder[1] = data_user[users_row][1]
        data_candi_with_builder[2] = data_user[users_row][2]

        appendData(trashcan_stack, data_candi_with_builder)
            
        
    
    # KITA HILANGKAN DARI DATA_USER
    data_user[users_row][0] = None
    data_user[users_row][1] = None
    data_user[users_row][2] = None
    
