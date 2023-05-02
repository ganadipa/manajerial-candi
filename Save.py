import os
os.chdir(os.path.dirname(__file__))
import sys
import time

import csvparser

from typing import List
matrixData = List[List[str]]

def save(data: List[matrixData]) -> None:
    
    data_user = data[0]
    data_candi = data[1]
    data_bahan_bangunan = data[2]
    
    print('Masukkan nama folder: ', end = '')
    folderInput = input()
    while folderInput == '':
        print('Anda tidak memasukkan nama folder dengan benar. Ulangi.')
        print('Masukkan nama folder: ', end = '')
        folderInput = input()
    
    print()
    print('Saving...')
    databaseFolder = os.path.join('database', folderInput)
    
    file_data_user = os.path.join(databaseFolder, 'user.csv')
    file_data_candi = os.path.join(databaseFolder, 'candi.csv')
    file_data_bahan_bangunan = os.path.join(databaseFolder, 'bahan_bangunan.csv')
    
    
    if not(os.path.isdir('database')):
        print('Membuat folder database...')
        time.sleep(0.5)
        os.makedirs('database')
    
    if not(os.path.isdir(databaseFolder)):
        print(f'Membuat folder {databaseFolder}...')
        time.sleep(0.5)
        os.makedirs(databaseFolder)
    
    print()
        
    if not(os.path.isfile(file_data_user)):
        print('Membuat file user.csv untuk menyimpan data-data user...')
    print('Memuat data-data user ke dalam user.csv...')
    time.sleep(0.5)
    csvparser.write_csv(file_data_user, data_user)
    
    
    print()
    
    if not(os.path.isfile(file_data_candi)):
        print('Membuat file candi.csv untuk menyimpan data-data candi...')
    print('Memuat data-data candi ke dalam candi.csv...')
    time.sleep(0.5)
    csvparser.write_csv(file_data_candi, data_candi)
    
    print()
    
    if not(os.path.isfile(file_data_bahan_bangunan)):
        print('Membuat file bahan_bangunan.csv untuk menyimpan data-data bahan bangunan...')
    print('Memuat data-data bahan bangunan ke dalam bahan_bangunan.csv...')
    time.sleep(0.5)
    csvparser.write_csv(file_data_bahan_bangunan, data_bahan_bangunan)
    
    
    sys.exit()
        
    