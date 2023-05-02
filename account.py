

loggedIn = ['False', '', '']

def login(usn, psw, data):
    
    if loggedIn[0] == 'True':
        print("Anda sudah log in ! ketik 'log out' untuk keluar.")
    else:
        
        row = 0
        data_usn = data[row][0]
        data_psw = data[row][1]
        data_role = data[row][2]
        
        while data_usn != '': #EOP
            if usn == data_usn:
                if psw == data_psw:
                    
                    loggedIn[0] = 'True'
                    loggedIn[1] = usn
                    loggedIn[2] = data_role
                    
                    print('\n')
                    print("Selamat datang, "+usn+"!")
                    print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    return usn
                else:
                    print("Password salah!")
                    return
            
            #UPDATE CHECKER
            row += 1
            data_usn = data[row][0]
            data_psw = data[row][1]
            data_role = data[row][2]

        print('Username tidak terdaftar!')
            
        
    ...

def logout():
    
    if loggedIn[0] == 'False':
        print('Anda belum log in!')
    else:
        print(f'Berhasil log out dari "{loggedIn[1]}."')
        loggedIn[0] = 'False'
        loggedIn[1] = ''
        loggedIn[2] = ''




