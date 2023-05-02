import csvparser
import os

def isAlphanumericOnly(word:str) -> bool:
    for i in range(len(word)):
        if custom_ord(word[i]) == -1:
            return False
    
    return True 

def valueOfStr(stri: str) -> int:
    res = 0
    length = len(stri)
    for i in range(length):
        res += custom_ord(stri[i]) * (123)**(length-i)
    
    return res
    
    
    
def custom_ord(k: str) -> int:
    alphanumeric = ['0','1','2','3','4','5','6','7','8', '9',
                    'A','B','C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N','O','P','Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    
                    'a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n','o','p','q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    ''
                    ]
    returnVal = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
           65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
           78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
           
           97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
           110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    
    i = 0
    while True:
        if alphanumeric[i] == k:
            break
        i += 1
        
        if alphanumeric[i] == '':
            return -1
    
    return returnVal[i]
     

def custom_chr(k: int) -> str:
    num = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
           65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
           78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
           
           97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
           110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    returnVal = ['0','1','2','3','4','5','6','7','8', '9',
                    'A','B','C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N','O','P','Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    
                    'a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n','o','p','q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    ''
                    ]
    
    i = 0
    while True:
        if num[i] == k:
            break
        i += 1
    
    return returnVal[i]

def appendData(data, lst):
    
    
    #MENGASUMSIKAN PANJANG LIST MASUKAN SELALU SAMA DENGAN BANYAKNYA KOLOM (VALID) PADA DATA.
    row = 0
    col = 0
    while True:
        cellData = data[row][col]
        
        if cellData == '' or cellData == None:
            break
        
        row +=  1
    
    lengthProperty = rowcolEff(data)[1]
    if lengthProperty == 5:
        if countData(data) >= 100:
            return
    for i in range(lengthProperty):
        data[row][i] = lst[i]
    

def append(lst1, lst2):
    index1 = getIndex('', lst1)
    index2 = getIndex('', lst2)
    
    for i in range(index2):
        lst1[index1+i] = lst2[i]
    
    
    
        
def countProperty(file, delimiter = ';'):
    
    if isinstance(file, list):
        col  =0
        while True:
            cellData = file[0][col]
            if cellData == '':
                break
            col += 1
        
        return col
        
    
    count = 0
    
    f = open(file, 'r')
    f.readline()
    cc = f.read(1)
    if cc == '':
        return 0
    else:
            
        while cc != '\n':
            
            if cc == delimiter:
                count += 1
            
            cc = f.read(1)
    
    f.close()
    return count + 1


def countData(file, delimiter = ';'):
    # MENGASUMSIKAN BARIS PALING AWAL DARI FILE SELALU HEADER.
    count = 0
    
    if isinstance(file, list):
        row = 0
        countNone = 0
        while True:
            cellData = file[row][0]
            if cellData == '':
                break
            
            if cellData is None:
                countNone +=1
            row += 1
                
                
        
        return row -1 - countNone
            
    f = open(file, 'r')
    f.readline()
    
    while True:
        cc = f.read(1)
        
        if cc == '' or cc == '\n':
            break
        
        count += 1
        f.readline()
    
    return count



def rowcolEff(data):
    cellData = data[0][0]
    
    colCount = 0
    while cellData != '':
        colCount += 1
        cellData = data[0][colCount]
    
    rowCount = 0
    while cellData != '':
        rowCount += 1
        cellData = data[rowCount][0]
    
    return (rowCount, colCount)

       
def listOfJin(data_user, role = 'all'):
    lst = ['' for i in range(102)]
    
    i = 0
    counter = 0
    while True:
        if role == 'all':
            if data_user[i][2] == 'jin_pembangun' or data_user[i][2] == 'jin_pengumpul':
                lst[counter] = data_user[i][0]
                counter += 1
        
        elif role == 'jin_pembangun':
            if data_user[i][2] == 'jin_pembangun':
                lst[counter] = data_user[i][0]
                counter += 1
            
        
        if data_user[i][0]== '' and data_user[i][1] == '' and data_user[i][2] == '':
            break
        
        i+= 1
        
    
    return lst

def lstOfCandi(data_candi):
    lst = ['' for i in range(countData(data_candi)+1)]
    i = 0
    k = 0
    while i < countData(data_candi):
        if data_candi[i+k+1][0] is not None:
            lst[i] = data_candi[i+k+1][0]
            i += 1
        k += 1
        
    return lst
    

def jin_most(data_user, data_candi, adj):
    #MEMBUAT LIST OF JIN PEMBANGUN
    lstOfNames = listOfJin(data_user)
    
    # MEMBUAT LIST YANG PANJANGNYA SAMA DENGAN PANJANG EFEKTIF dari "lstOfNames" + 1 
    # TERDIRI DARI N DATA SKOR, DAN MARK BERUPA -1
    length = getIndex('', lstOfNames )
    lstOfScores = [-1 for i in range(length+1)]
    for i in range(length):
        lstOfScores[i] += 1
    
    # lstOfScores (initially) = [0,0,0,..., 0,0,-1]

    #ITERATE SELURUH DATA CANDI DAN MELIHAT NAMA PEMBUATNYA, KEMUDIAN MENGAMBIL INDEKS DARI NAMA TERSEBUT PADA "lstOfNames"
    #KEMUDIAN MENAMBAHKAN 1 POIN PADA "lstOfScores" PADA INDEKS YANG TELAH DIDAPATKAN. DENGAN KATA LAIN, INDEKS NAMANYA ADALAH INDEKS SKORNYA.
    i = 1
    k = 0
    while data_candi[i+k][1] is None:
        k += 1
        
    builderName = data_candi[i+k][1]
    
    while builderName != '':
        index = getIndex(builderName, lstOfNames)
        
        lstOfScores[index] += 1
        
        i += 1
        while data_candi[i+k][1] is None:
            k += 1
        builderName = data_candi[i+k][1]
    
    if adj == 'hardworking':
        maxi = maxValue(lstOfScores)
        hardworkerLst = namesThatHaveScore(maxi, lstOfNames, lstOfScores)
        
        return minValue(hardworkerLst, type = 'str')
    
    elif adj == 'lazy':
        mini = minValue(lstOfScores)
        loaferLst = namesThatHaveScore(mini, lstOfNames, lstOfScores)

        return minValue(loaferLst, type = 'str')
        

def namesThatHaveScore(n, lstOfNames, lstOfScores):
    lst = ['' for i in range(102)]
    
    count = 0
    i = 0
    num = lstOfScores[i]
    while num != -1:
        if num == n:
            lst[count] = lstOfNames[i]
        
        i += 1
        num = lstOfScores[i]
    
    return lst
        


def getIndex(search: str, 
             array:list , 
             type:str = '1d', 
             in_row:int | None = None, 
             in_col:int | None = None) -> int:
    # FUNGSI INI DIGUNAKAN UNTUK MENDAPATKAN INDEX PERTAMA YANG ELEMENNYA BERNILAI SEARCH. APABILA TIDAK DITEMUKAN,
    # MENGEMBALIKAN NILAI 99999
    # di dalam array.
    if type == '1d':
        i = 0
        name = array[i]
        while name != search:
            
            i += 1
            name = array[i]
        
        return i
    
    elif type == '2d':
        if in_row == None and in_col == None:
            for row in range(countData(array)):
                for col in range(countProperty(array)):
                    if array[row][col] == search:
                        return (row, col)
        
        else:
            if in_row == None:
                row = 0
                cellData = array[row][in_col]
                while cellData != search and cellData !='' :
                    
                    
                    row += 1
                    cellData = array[row][in_col]
                
                if search == '':
                    return row
                
                if cellData == '':
                    return 99999
                return row
            
            else: # in_col == None  
                col = 0
                cellData = array[in_row][col]
                while cellData != search and cellData !='':
                    
                    
                    col += 1
                    cellData = array[in_row][col]
                
                if search == '':
                    return row
                
                if cellData == '':
                    return 99999
                
                return col
    else:
        return -99999 #Tidak ada type selain 1d dan 2d

def maxValue(arr, type = 'int'):
    if type == 'int':
        #MARKNYA ADALAH -1, MENGASUMSIKAN ARRAY BERISI INTEGER BILANGAN CACAH, JIKA TIDAK ADA ANGKA, MENGEMBALIKAN -1.
        maxi = -1
        i = 0
        num = arr[i]
        while num != -1:
            if maxi < num:
                maxi = num
            
            i += 1
            num = arr[i]
        
        return maxi
    else:
        print('ALGORITMA UNTUK TYPE LAIN BLM DIBUAT.')

def minValue(arr, type = 'int'):
    if type == 'int':
        #MARKNYA ADALAH -1, MENGASUMSIKAN ARRAY BERISI INTEGER BILANGAN CACAH, JIKA TIDAK ADA ANGKA, MENGEMBALIKAN -1.
        mini = float('inf') #APAKAH BOLEH?
        i = 0
        num = arr[i]
        while num != -1:
            if mini > num:
                mini = num
            
            i += 1
            num = arr[i]
        
        if mini == float('inf'):
            return -1
        
        return int(mini)
    elif type == 'str':
        # MARKNYA ADALAH '', ARRAY TIDAK BOLEH KOSONG.
        i = 0
        stri = arr[i]
        mini = stri
        while stri != '':
            if valueOfStr(mini) > valueOfStr(stri):
                mini = stri
            
            i += 1
            stri = arr[i]
        
        return mini
    else:
        print('ALGORITMA UNTUK TYPE LAIN BLM DIBUAT.')
        

    
        
            
        
    
    ...

def sumData(data, row = None, col = None):
    # MENJUMLAHKAN SEMUA DATA PADA KOLOM TERTENTU ATAU BARIS TERTENTU MENGASUMSIKAN PENGGUNA FUNGSI MENGETAHUI APA DAMPAKNYA BILA ADA DATA
    # YANG TIDAK BISA DIKONVERSI MENJADI INTEGER.
    if row == None and col == None:
        return
    else:
        if row == None:
            sum = 0
            length = countData(data)
            for i in range(length):
                if data[i+1][col] is not None:
                    sum += int(data[i+1][col])
        else:
            sum = 0
            length = countProperty(data)
            for i in range(length):
                if data[row][i+1] is not None:
                    sum += int(data[row][i+1])
        
        return sum

def hargaCandi(id, data_candi):
    row = getIndex(id, data_candi, type = '2d', in_col=0)
    
    neededSand = int(data_candi[row][2])
    neededRock = int(data_candi[row][3])
    neededWater = int(data_candi[row][4])
    
    cost = 10000*neededSand + 15000*neededRock + 7500*neededWater
    return cost
    
def candi_most(data_candi, adj):
    #MEMBUAT LIST OF CANDI
    listOfID = lstOfCandi(data_candi)
    
    # MEMBUAT LIST YANG PANJANGNYA SAMA DENGAN PANJANG EFEKTIF dari "lstOfNames" + 1 
    # TERDIRI DARI N DATA SKOR, DAN MARK BERUPA -1
    length = getIndex('', listOfID )
    listOfPrice = [-1 for i in range(length+1)]
    for i in range(length):
        listOfPrice[i] += 1
    
    for i in range(length):
        IDCandi = listOfID[i]
        listOfPrice[i] = hargaCandi(IDCandi, data_candi)
    if adj == 'murah':
        mini = minValue(listOfPrice)
        indexMini = getIndex(mini, listOfPrice)
        return listOfID[indexMini]
    
    elif adj == 'mahal':
        maxi = maxValue(listOfPrice)
        indexMaxi = getIndex(maxi, listOfPrice)
        return listOfID[indexMaxi]
    
    
    

#####################
def roleJin(usnJin, data_user):
    # PREKONDISIR USNJIN ADA DI DALAM DATA_USER
    rowIndex = getIndex(usnJin, data_user, type = '2d', in_col = 0 )
    return data_user[rowIndex][2]
    
def inputUsernameJin(data_user):
    
    print("Masukkan username jin: ", end= '')
    usnJin = input()
    while doesUsernameExist(usnJin, in_data=data_user, role = 'all'):
        print('Username "'+usnJin+'" sudah diambil!')
        print('\n')
        print("Masukkan username jin: ", end = '')
        usnJin = input()
    
    while not(isAlphanumericOnly(usnJin)):
        print('Username harus hanya terdiri atas alphanumeric character!')
        print('\n')
        print("Masukkan username jin: ", end = '')
        usnJin = input()
    
    return usnJin

def inputPasswordJin():
    print("Masukkan password jin: ", end = '' )
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

def countJin(data, type = 'all'):
    
    colIndex = getIndex('role', data, type = '2d', in_row=0)
    if colIndex == -1:
        print('DATA YANG DIMASUKKAN BUKAN DATA USER !')
        return
    
    i = 0
    checker = data[i][colIndex]
    
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
    else: # type == 'jin_pengumpul'
        return countJin - countJin_pembangun
        
        
    
def isJin(role):
    if role == 'jin_pembangun' or role == 'jin_pengumpul':
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

def listOf(type, fromData):
    result = ['' for i in range(102)]
    colIndex = getIndex(type, fromData, type = '2d', in_row = 0)
    
    
    i = 1
    datum = fromData[i][colIndex]
    
    while datum != '':
        result[i-1] = datum
        
        
        i += 1
        datum = fromData[i][colIndex]
    
    return result
        
    
    
def doesUsernameExist(username, in_data = None, role = None):
    if in_data[0][0] == 'id':
        propertyUsername = 'pembuat'
    elif in_data[0][0] == 'username':
        propertyUsername = 'username'
        
    colIndex = getIndex(propertyUsername, in_data, type = '2d', in_row=0)
    check = False
    
    if colIndex == 1:
        for i in range(countData(in_data)):
            if username == in_data[i][1]:
                check = True
                break
    
    if colIndex == 0:
    
        if role == 'jin': #UNTUK IN_DATA BERUPA DATA_USER
            for i in range(countData(in_data)-2): # TIDAK MENGECEK BAGIAN BONDOWOSO DAN RORO 
                if username == in_data[i+3][colIndex]:
                    check = True
        
        if role == 'all': #UNTUK IN_DATA BERUPA DATA_USER
            for i in range(countData(in_data)):
                if username == in_data[i+1][colIndex]:
                    check = True
        
    return check

def validateYN(expr: str) -> str:
    print(expr, end = '')
    YN = input()
    while YN != 'Y' or YN != 'N' or YN != 'y' or YN != 'n' :
        print(expr, end = '')
        YN = input()
    return YN

if __name__ == '__main__':
    print(valueOfStr('AC'))
    print(valueOfStr('Ab'))
    print(valueOfStr('AC') < valueOfStr('Ab'))