import os
os.chdir(os.path.dirname(__file__))

from csvparser import csv_reader



def roleJin(usnJin):
    # PREKONDISIR USNJIN ADA DI DALAM DATA_USER
    data_user = csv_reader('csv_files/user.csv',';')
    i = 0
    while True:                                         # CAN BE BUILT INTO A FUNCTION GETINDEX()
        check_usn = data_user[i][0]
        if check_usn == usnJin:
            break
        i+= 1
    
    return data_user[i][2]
    
def inputUsernameJin():
    
    print("Masukkan username jin: ", end= '')
    usnJin = input()
    while doesUsernameExist(usnJin, 'user.csv'):
        print('Username "'+usnJin+'" sudah diambil!')
        print('\n')
        print("Masukkan username jin: ", end = '')
        usnJin = input()
    
    return usnJin

def inputPasswordJin():
    print("Masukkan password jin: ")
    pswJin = input()
    while not(isPasswordValid(pswJin)):
        print('Password panjangnya harus 5-25 karakter!')
        print("Masukkan password jin: ", end = '')
        pswJin = input()
    return pswJin
        
    
def isPasswordValid(password):
    check = True
    if len(password) > 25 or len(password)<5:
        check = False
    return check

def countJin(type = 'all'):
    
    data = csv_reader('csv_files/user.csv', ';')
    i = 0
    checker = data[i][2]
    
    countJin = 0
    countJin_pembangun = 0
    
    while checker != '':
        if isJin(checker):
            countJin += 1
        
        if isJin_pembangun(checker):
            countJin_pembangun += 1
        
        i += 1
        checker = data[i][2]
    if type == 'all':
        return countJin
    elif type == 'jin_pembangun':
        return countJin_pembangun
    elif type == 'jin_pengumpul':
        return countJin - countJin_pembangun
        
        
    
def isJin(role):
    if role[0] == 'j' and role[1] == 'i' and role[2] == 'n':
        return True
    else:
        return False

def isJin_pembangun(role):
    if isJin(role):
            
        if role[6] == 'm':
            return True
        elif role[6] == 'n':
            return False

def isJin_pengumpul(role): #MENGASUMSIKAN HANYA ADA 2 JIN
    if isJin_pembangun(role):
        return False
    else:
        return True

# LISTOF AND DOESUSERNAMEEXIST FUNCTIONS HAVE BAD CODE BECAUSE OF THE FILENAME.
def listOf(type, fromData):
    result = ['' for i in range(102)]

    
    numberrow = 0
    if fromData == 'user.csv':
        data_users = csv_reader('csv_files/user.csv', ';')

        if type == 'username':
            usn = data_users[numberrow][0]
            while usn != '':
                result[numberrow] = usn
                numberrow+= 1
                usn = data_users[numberrow][0]
    
    elif fromData == 'candi.csv':
        data_candi = csv_reader('csv_files/candi.csv', ';')
        
        if type == 'username':
            usn = data_candi[numberrow][1]
            while usn != '':
                result[numberrow] = usn
                numberrow+= 1
                usn = data_candi[numberrow][1]
    
    return result
            
        
    
    
def doesUsernameExist(username, filename):
    if filename == 'user.csv':
        usnList = listOf('username','user.csv')
    elif filename == 'candi.csv':
        usnList = listOf('username', 'candi.csv')
        
    check = False
    init = 0
    usnChecker = usnList[init]
    
    while usnChecker != '':
        if usnChecker == username:
            check = True
            break
        init += 1
        usnChecker = usnList[init]
    
    return check

