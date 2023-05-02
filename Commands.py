import os
os.chdir(os.path.dirname(__file__))
import argparse
import sys
from typing import List

import Login
import Logout

import Summonjin
import Hapusjin
import Ubahjin

import Kumpul
import Bangun

import Batch
import Laporanjin
import Laporancandi

import Hancurkancandi
import Ayamberkokok

import Save
import Help
import Exit

import csvparser
from Helper import countJin
import Meditasi
import tictactoe


dataMatrix = List[List[str]]

def run(command: str, database: List[dataMatrix]) -> None:
    
    status_info = database[3][1]
    
    if command == 'login':
        if status_info[0] == 'True':
            print("Login gagal!")
            print(f"Anda telah login dengan username {status_info[1]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        else:
            Login.login(database)
        
    
    elif command == 'logout':
        if status_info[0] == 'False':
            print('Logout gagal! \nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout')
        else:
            Logout.logout(database)
    
    elif command == 'summonjin':
        if status_info[2] == 'bandung_bondowoso' or status_info[2] == 'bandung_bondowoso_enlightened':
            Summonjin.summonjin(database)
        else:
            print('Anda tidak berwenang untuk menggunakan kekuatan sang Bondowoso!')
    
    elif command == 'hapusjin':
        if status_info[2] == 'bandung_bondowoso' or status_info[2] == 'bandung_bondowoso_enlightened':
            Hapusjin.hapusjin(database)
        else:
            print('Anda tidak berwenang untuk menggunakan kekuatan sang Bondowoso!')
    
    elif command == 'ubahjin': #REKURSI
        if status_info[2] == 'bandung_bondowoso' or status_info[2] == 'bandung_bondowoso_enlightened':
            print('Masukkan username jin: ', end = '')
            usnJin = input()
            Ubahjin.ubahjin_recursion(usnJin, database)
        else:
            print('Anda tidak berwenang untuk menggunakan kekuatan sang Bondowoso!')
        
        print()
        
    elif command == 'kumpul':
        if status_info[2] == 'jin_pengumpul':
            Kumpul.kumpul(database)
        else:
            print('kekuatan ini hanya dimiliki oleh pemilik role jin "Pengumpul".')
    
    elif command == 'bangun':
        if status_info[2] == 'jin_pembangun':
            Bangun.bangun(status_info[1], database)
        else:
            print('kekuatan ini hanya dimiliki oleh pemilik role jin "Pembangun".')
    
    elif command == 'batchkumpul': #REKURSI
        if status_info[2] == 'bandung_bondowoso' or status_info[2] == 'bandung_bondowoso_enlightened':
            totalJin = countJin(database[0], type = 'jin_pengumpul')
            if totalJin == 0:
                print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')
            else:
                materialsCollected = Batch.batchkumpul_recursion(database, totalJin)
                print(f'Jin menemukan total {materialsCollected[0]} pasir, {materialsCollected[1]} batu, dan {materialsCollected[2]} air.')
        else:
            print('Anda tidak berwenang untuk menggunakan kekuatan sang Bondowoso!')
    
    elif command == 'batchbangun':
        if status_info[2] == 'bandung_bondowoso' or status_info[2] == 'bandung_bondowoso_enlightened':
            Batch.batchbangun(database)
        else:
            print('Anda tidak berwenang untuk menggunakan kekuatan sang Bondowoso!')
    
    elif command == 'laporanjin':
        if status_info[2] == 'bandung_bondowoso' or status_info[2] == 'bandung_bondowoso_enlightened':
            Laporanjin.laporanjin(database)
        else:
            print('Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.')
    
    elif command == 'laporancandi':
        if status_info[2] == 'bandung_bondowoso' or status_info[2] == 'bandung_bondowoso_enlightened':
            Laporancandi.laporancandi(database)
        else:
            print('Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.')
    
    elif command == 'hancurkancandi': # REKURSI
        if status_info[2] == 'roro_jonggrang':
            print('Masukkan ID candi: ',end = '')
            idCandi = input()
            Hancurkancandi.hancurkancandi_recursion(database, idCandi)
        else:
            print('Anda tidak bisa menghancurkan candi Bondowoso.')
    
    elif command == 'ayamberkokok': # REKURSI
        if status_info[2] == 'roro_jonggrang':
            print('Kukuruyuk.. Kukuruyuk..')
            print()
            doesRoroWin = Ayamberkokok.ayamberkokok_recursion(database)
            if doesRoroWin == True:
                print('Selamat, Roro Jonggrang memenangkan permainan!')
                print()

                print('*Bandung Bondowoso angry noise*')
                print('Roro Jonggrang dikutuk menjadi candi.')
            else:
                print('Yah, Bandung Bondowoso memenangkan permainan!')
            
            sys.exit()
        
        else:
            print('Anda bukan roro.')
    
    elif command == 'save':
        Save.save(database)
        
    elif command == 'help':
        Help.help(status_info[2])
    
    elif command == 'exit': # REKURSI
        Exit.exit(database)
    
    elif command == 'meditasi':
        if status_info[2] == 'bandung_bondowoso':
            Meditasi.meditasi(database)
            print('Meditasi selesai. Bondowoso tercerahkan ! didapatkan skill undo hilangkan jin. skill ini dapat dilakukan')
            print('dengan mengetik "undo".')
        elif status_info[2] == 'bandung_bondowo_enlightened':
            print('Meditasi selesai.')
        else:
            print('Hanya dapat dilakukan oleh Bondowoso.')
            
    elif command == 'undo':
        if status_info[2] == 'bandung_bondowoso':
            print('Silakan melakukan meditasi terlebih dahulu, Bandung.')
        elif status_info[2] == 'bandung_bondowoso_enlightened':
            Meditasi.undo(database)
        else:
            print('Tidak ada command "undo"')
            
    
    elif command == 'inginmain':
        if status_info[2] == 'bandung_bondowoso' or status_info[2] == 'bandung_bondowoso_enlightened':
            print('Bondowoso merasa bosan ya?')
            print('Mari bermain tictactoe! Apakah Bondowoso ingin bermain dengan anak kecil atau dengan jin yang super cerdas?')
            print('(1.) Anak kecil')
            print('(2.) Jin cerdas')
            print('pilihan: ', end = '')
            ans = input()
            while ans != '1' and ans != '2':
                print('Tidak ada lawan selain kedua lawan di atas...')
                print('Silakan pilih nomor 1 atau 2. Pilihan: ', end = '')
                ans = input()
            print()
            print('Alur:' )
            if ans == '1':
                print('Bondowoso: "HOI ANAK KECIL AYO BERMAIN TICTACTOE, KALAU TIDAK MAU NANTI AKU KUTUK MENJADI CANDI!"')
                print('Anak kecil: "Yaudah, tapi 1 game aja."')
                print()
                tictactoe.play(opponent = 'bocil')
                print('*Anak kecil langsung hilang*')
            
            if ans == '2':
                print('Bondowoso: *summon jin yang super cerdas*')
                print('Jin cerdas: "Selamat siang, Bondowoso, akan ku turuti permintaan mu untuk bermain tictactoe dengan ku. Tetapi jika')
                print('             engkau tidak menang, aku akan pergi, karena aku sedang sibuk.')
                print()
                tictactoe.play(opponent = 'jin-cerdas')
                print('Jin cerdas: "Karena engkau tidak menang, maka aku hilang." *poof*')
        
        else:
            print('Tidak ada command "inginmain"')
            
                
                
                            
            
            
            
            
            
    
    
    
    # elif command == 'dev': # HANYA SEBAGAI CHECKER
    #     while True:
    #         devTools =input('>>> developer tools: ')
    #         if devTools == 'out':
    #             break
    #         elif devTools == 'infodata':
    #             print(f'Info status_info:')
    #             print(database[3])
                
    #             print(f'Matriks data_user saat ini:')
    #             printData(database[0])
                
    #             print(f'Matriks data_candi saat ini:')
    #             printData(database[1])
                
    #             print(f'Matriks data_bahan_bangunan saat ini:')
    #             printData(database[2])
                
    #             print(f'Stack: ')
    #             printData(database[4])
            
    #         elif devTools == 'login':
    #             print('Role: ', end = '')
    #             role = input()
    #             status_info[0] = True
    #             status_info[2] = role
            
    
    else:
        print(f'Tidak ada command "{command}".')
    
    print()
        

def load(filename, var):
    
    # FUNGSI INI BERGUNA UNTUK MENGELOAD database PADA FILE "filename" DALAM BENTUK LIST KE DALAM VAR.
    
    
    data = csvparser.read_csv(filename) #MEMBACA database PADA FILE
    
    row = 0
    while True:
        
        col = 0
        celldata = data[row][col]
        while celldata != '':
            var[row][col] = celldata
            
            col += 1
            celldata = data[row][col]
            
        row += 1
        if data[row][0] == '':
            break
        
        
def printData(data):
    row = 0
    while True:
        
        col = 0
        celldata = data[row][col]
        
        print(f'{row+1}.', end = ' ')
        while celldata != '':
            print(celldata, end = ' ')
            
            col += 1
            celldata = data[row][col]
        
        print()
        row += 1
        if data[row][0] == '':
            break

def validate_folder():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type = str, help = 'The name of the folder that contains the database.')
    parsed_args = parser.parse_args()
    
    databaseFolder = parsed_args.folder
    if os.path.exists(databaseFolder) and os.path.isdir(databaseFolder):
        print(f"The folder '{databaseFolder}' exists.")
    else:
        print(f"Folder “{databaseFolder}” tidak ditemukan.")
        return None
    
        