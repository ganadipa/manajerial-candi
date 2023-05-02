from Helper import countJin, jin_most
from typing import List
matrixData = List[List[str]]

def laporanjin(database: List[matrixData]) -> None:
    data_user = database[0]
    data_candi = database[1]
    data_bahan_bangunan = database[2]
    
    
    #OUTPUT
    print()
    print(f"> Total Jin: {countJin(data_user, type = 'all')}" )
    print(f"> Total Jin Pengumpul: {countJin(data_user, type = 'jin_pengumpul')}" )
    print(f"> Total Jin Pembangun: {countJin(data_user, type = 'jin_pembangun')}" )
    if countJin(data_user, type='jin_pembangun') == 0:
        print(f"> Jin Terajin: -")
        print(f"> Jin Terajin: -")
    else:
        print(f"> Jin Terajin: {jin_most(data_user, data_candi, adj = 'hardworking')}" )
        print(f"> Jin Termalas: {jin_most(data_user, data_candi, adj = 'lazy')}" )
    print(f"> Jumlah Pasir: {data_bahan_bangunan[1][2]} unit" )
    print(f"> Jumlah Batu: {data_bahan_bangunan[2][2]} unit" )
    print(f"> Jumlah Air: {data_bahan_bangunan[3][2]} unit" )