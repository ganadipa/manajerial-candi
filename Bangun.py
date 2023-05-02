import LCG
import os
from Helper import countData
os.chdir(os.path.dirname(__file__))

from typing import List
matrixData = List[List[str]]

def bangun(usnJin: str, database: List[matrixData]) -> None:
    
    data_candi = database[1]
    data_bahan_bangunan = database[2]
    totalCandi = countData(data_candi)
    
    availableSand = int(data_bahan_bangunan[1][2])
    availableRock = int(data_bahan_bangunan[2][2])
    availableWater = int(data_bahan_bangunan[3][2])
    
    materialsNeeded = LCG.randsample(3, 0, 5)
    neededSand = int(materialsNeeded[0])
    neededRock = int(materialsNeeded[1])
    neededWater = int(materialsNeeded[2])
    
    print('# Men-generate bahan bangunan (',materialsNeeded[0],'pasir,',materialsNeeded[1],'batu, dan ',materialsNeeded[2],'air)')
    print(f'# Saat ini kita punya {availableSand} pasir, {availableRock} batu, dan {availableWater} air.')
    if availableSand < neededSand or availableRock < neededRock or availableWater < neededWater:
        print('Bahan bangunan tidak mencukupi.')
        print('Candi tidak bisa dibangun!')
    else:
        data_bahan_bangunan[1][2] = str(int(data_bahan_bangunan[1][2])- neededSand)
        data_bahan_bangunan[2][2] = str(int(data_bahan_bangunan[2][2])- neededRock)
        data_bahan_bangunan[3][2] = str(int(data_bahan_bangunan[3][2])- neededWater)

        i = 0 
        while i< 100:
            if data_candi[i][0] == '' or data_candi[i][0] == None:
                data_candi[i][0] = str(i)
                data_candi[i][1] = str(usnJin)
                data_candi[i][2] = str(neededSand)
                data_candi[i][3] = str(neededRock)
                data_candi[i][4] = str(neededWater)
                break
            
            i += 1


        # Jika i == 100, artinya jumlah candi sudah ada 100 dengan id 0,1,2,...,99. maka data candi
        # tidak dimasukkin ke dalam CSV.
        
        print('Candi berhasil dibangun.')
        if totalCandi < 100:
            totalCandi += 1
        
        print(f'Sisa candi yang perlu dibangun: {100-totalCandi}')
        print()
