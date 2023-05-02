import os
os.chdir(os.path.dirname(__file__))

import argparse
import sys
import time

def get_database_folder():
    
    parser = argparse.ArgumentParser(
        description='Welcome to "manajerial candi"',
        usage = 'python main.py <nama_folder>'
    )
    parser.add_argument(
        "folder",
        type = str,
        help = "Nama folder yang menyimpan database.",
        nargs = '?'
    )
    
    
    parsed_args = parser.parse_args()
    
    folder_name = parsed_args.folder
    if folder_name is None:
        print()
        print('Tidak ada nama folder yang diberikan!')
        print()
        print('Usage: python main.py <nama_folder>')
        sys.exit()
    folder_path = os.path.join('database', folder_name)
    
    
    file_user = os.path.join(folder_path, 'user.csv')
    file_candi = os.path.join(folder_path, 'candi.csv')
    file_bahan_bangunan = os.path.join(folder_path, 'bahan_bangunan.csv')
    

    if os.path.isdir(folder_path):
        if os.path.isfile(file_user) and os.path.isfile(file_candi) and os.path.isfile(file_bahan_bangunan):
            print()
            print('Loading...')
            time.sleep(0.5)
            return folder_path
        else:
            print()
            print(f'Folder {folder_path} ditemukan, tetapi tidak memuat file penyimpanan.')
            sys.exit()
    else:
        print()
        print(f'Folder “{folder_path}” tidak ditemukan.')
        sys.exit()