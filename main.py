
import argparse
import os
os.chdir(os.path.dirname(__file__))
from getdatabasefolder import get_database_folder
import Commands

data_user = [['' for i in range(10)] for i in range(1000)] # INISIALISASI ARRAY
data_candi = [['' for i in range(10)] for i in range(1000)] # INISIALISASI ARRAY
data_bahan_bangunan = [['' for i in range(10)] for i in range(1000)] # INISIALISASI ARRAY
trashcan_stack = [['' for i in range(10)] for i in range(1000)] #AKAN MENGADOSPI KONSEP STACK: FILO (FIRST IN LAST OUT)
status_matrix = [
    ['loggedIn', 'username', 'role'],
    ['False', '', '']
    ]


databaseFolder = get_database_folder()
file_data_user = os.path.join(databaseFolder, 'user.csv')
file_data_candi = os.path.join(databaseFolder, 'candi.csv')
file_data_bahan_bangunan = os.path.join(databaseFolder, 'bahan_bangunan.csv')
trashcan_stack[0] = ['username', 'password', 'role', 'id', 'pembuat', 'pasir', 'batu', 'air', '', '']

# FUNGSI LOAD ADA DI FILE COMMANDS.PY
Commands.load(file_data_user, data_user)
Commands.load(file_data_candi, data_candi)
Commands.load(file_data_bahan_bangunan, data_bahan_bangunan)

print(f'Data dari folder penyimpanan "{databaseFolder}" telah di-load ke dalam program.')
print(f'Selamat datang di program "manajerial candi" ! ')
print(f'Ketik "help" untuk melihat command apa saja yang dapat dilakukan. ')
print()

while True:
    masukan = input(">>> ")
    Commands.run(masukan, database = [data_user, data_candi, data_bahan_bangunan, status_matrix, trashcan_stack])