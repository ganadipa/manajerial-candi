import os
os.chdir(os.path.dirname(__file__))
from typing import List
matrixData = List[List[str]]

def login(database: List[matrixData]) -> None:
    print('Username: ', end = '')
    usnInput = input()
    
    print('Password: ', end = '')
    pswInput = input()
    
    data_user = database[0]
    data_status = database[3][1]
    
    row = 1
    data_usn = data_user[row][0]
    data_psw = data_user[row][1]
    data_role = data_user[row][2]
    
    checkUsn = False
    while data_usn != '': #EOP
        if usnInput == data_usn:
            checkUsn = True
            if pswInput == data_psw:
                
                data_status[0] = 'True'
                data_status[1] = usnInput
                data_status[2] = data_role
                
                print()
                print("Selamat datang, "+usnInput+"!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
            else:
                print("Password salah!")
        
        # UPDATE DATA_USER
        row += 1
        data_usn = data_user[row][0]
        data_psw = data_user[row][1]
        data_role = data_user[row][2]

    if checkUsn == False:
        print('Username tidak terdaftar!')
        
        