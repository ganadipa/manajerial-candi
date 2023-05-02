from Helper import hargaCandi, candi_most, countData, sumData

from typing import List
matrixData = List[List[str]]

def laporancandi(database: List[matrixData]) -> None:
    
    
    data_candi = database[1]
    
        
    
    
    #OUTPUT
    print()
    print(f"> Total Candi: {countData(data_candi)}" )
    print(f"> Total Pasir yang digunakan: {sumData(data_candi, col = 2)}" )
    print(f"> Total Batu yang digunakan: {sumData(data_candi, col = 3)}" )
    print(f"> Total air yang digunakan: {sumData(data_candi, col = 4)}" )
    if countData(data_candi) == 0:
        print('> ID Candi Termahal: -')
        print('> ID Candi Termurah: -')
    else:
        hargaTermahal = hargaCandi(candi_most(data_candi, adj = 'mahal'), data_candi)
        hargaTermurah = hargaCandi(candi_most(data_candi, adj = 'murah'), data_candi)
        print(f"> ID Candi Termahal: {candi_most(data_candi, adj = 'mahal')} (Rp {hargaTermahal})" )
        print(f"> ID Candi Termurah: {candi_most(data_candi, adj = 'murah')} (Rp {hargaTermurah})" )