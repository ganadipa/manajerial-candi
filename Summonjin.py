from Helper import countJin, inputPasswordJin, inputUsernameJin, appendData
from typing import List
matrixData = List[List[str]]

def summonjin(database: List[matrixData])-> None:
    
    data_user = database[0]
    
    if countJin(data_user) == 100:
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
        return
    else:
        print('Jenis jin yang dapat dipanggil: ')
        print('(1) Pengumpul - Bertugas mengumpulkan bahan bangunan')
        print('(2) Pembangun - Bertugas membangun candi')
        print()
        
        
        # MEMVALIDASI INPUT NOMOR JIN YANG INGIN DI-SUMMON
        print('Masukkan nomor jenis jin yang ingin dipanggil: ', end = '')
        n = input()
        while n != '1' and n != '2':
            print()
            print('Tidak ada jenis jin bernomor "'+n+'" !')
            print()
            print('Masukkan nomor jenis jin yang ingin dipanggil: ', end = '')
            n = int(input())
            
        if n == '1':
            print('Memilih jin “Pengumpul”.')
            roleJin = 'jin_pengumpul'
        
        else:
            print('Memilih jin "Pembangun".')
            roleJin = 'jin_pembangun'
            
        print()
        usnJin = inputUsernameJin(data_user) #INPUT MENGGUNAKAN FUNGSI INI SUDAH TERVALIDASI 
        pswJin = inputPasswordJin() #INPUT MENGGUNAKAN FUNGSI INI SUDAH TERVALIDASI 
        
        
        print('Mengumpulkan sesajen...')
        print('Menyerahkan sesajen...')
        print('Membacakan mantra...')
        print()
        
        print('Jin', usnJin, 'berhasil dipanggil!')
        print()
        
        infoJin = [usnJin, pswJin, roleJin]
        
        appendData(data_user, infoJin)