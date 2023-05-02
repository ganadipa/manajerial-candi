import LCG
from csvparser import read_csv
import os
from Helper import countJin, listOfJin, countData
os.chdir(os.path.dirname(__file__))

from typing import List, Optional, Tuple
matrixData = List[List[str]]

def batchkumpul(database:List[matrixData], totaljin: int) -> List[int]:
    
    data_bahan_bangunan = database[2]
    
    print(f'Mengerahkan {totaljin} jin untuk mengumpulkan bahan.')
    
    data_bahan_bangunan[1][2] = int(data_bahan_bangunan[1][2])
    data_bahan_bangunan[2][2] = int(data_bahan_bangunan[2][2])
    data_bahan_bangunan[3][2] = int(data_bahan_bangunan[3][2])
    
    sandCollected = 0
    rockCollected = 0
    waterCollected = 0
    
    for i in range(totaljin):
        materialsCollected = LCG.randsample(3, 0, 5)
        sandCollected += materialsCollected[0]
        rockCollected += materialsCollected[1]
        waterCollected += materialsCollected[2]

    
    data_bahan_bangunan[1][2] = str(int(data_bahan_bangunan[1][2])+sandCollected)
    data_bahan_bangunan[2][2] = str(int(data_bahan_bangunan[2][2])+rockCollected)
    data_bahan_bangunan[3][2] = str(int(data_bahan_bangunan[3][2])+waterCollected)
    
    return [sandCollected, rockCollected, waterCollected]
    
        
def batchkumpul_recursion(database: List[matrixData], 
                          totaljin: int,  
                          totalWorked: Optional[int] = 0,
                          collectedMaterials:Optional[Tuple[int]] = (0,0,0)
                          ) -> List[int]:
    
    data_bahan_bangunan = database[2]
    
    if totaljin == 0: # BASE CASE
        print(f'Mengerahkan {totalWorked} jin untuk mengumpulkan bahan.')
        data_bahan_bangunan[1][2] = str(collectedMaterials[0] + int(data_bahan_bangunan[1][2]))
        data_bahan_bangunan[2][2] = str(collectedMaterials[1] + int(data_bahan_bangunan[2][2]))
        data_bahan_bangunan[3][2] = str(collectedMaterials[2] + int(data_bahan_bangunan[3][2]))
        return collectedMaterials

    listOfMaterials = LCG.randsample(3,0,5)
    sandCollected = listOfMaterials[0]
    rockCollected = listOfMaterials[1]
    waterCollected = listOfMaterials[2]
    
    collectedMaterials = (collectedMaterials[0] + sandCollected,
                          collectedMaterials[1]+rockCollected,
                          collectedMaterials[2]+waterCollected)
        
    return batchkumpul_recursion(database, totaljin-1,totalWorked+1, collectedMaterials)
        
def batchbangun(database: List[matrixData]) -> None:
    
    data_user = database[0]
    data_candi = database[1]
    data_bahan_bangunan = database[2]
    
    
    countJinPembangun = countJin(data_user,'jin_pembangun')
    
    if countJinPembangun == 0:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
        return
    
    lstOfRandomInteger = LCG.randsample(countJinPembangun, 0, countJinPembangun-1)
    namesJinPembangun = listOfJin(data_user, role = 'jin_pembangun')
    
    matrixMaterialsNeeded = [[0 for i in range(3)] for i in range(102)]
    
    availableSand = int(data_bahan_bangunan[1][2])
    availableRock = int(data_bahan_bangunan[2][2])
    availableWater = int(data_bahan_bangunan[3][2])
    
    neededSand = 0
    neededRock = 0
    neededWater = 0
    
    for i in range(countJinPembangun):
        materialsNeeded = LCG.randsample(3,1,5)
        neededSand += materialsNeeded[0]
        neededRock += materialsNeeded[1]
        neededWater += materialsNeeded[2]

        matrixMaterialsNeeded[i][0] = materialsNeeded[0]
        matrixMaterialsNeeded[i][1] = materialsNeeded[1]
        matrixMaterialsNeeded[i][2] = materialsNeeded[2]
    
    print(f'Mengerahkan {countJinPembangun} jin untuk membangun candi dengan total bahan {neededSand} pasir, {neededRock} batu, dan {neededWater} air.')
    
    if availableSand < neededSand or availableRock < neededRock or availableWater < neededWater:
        print('Bangun gagal. Kurang ', end ='')
        
        if availableSand < neededSand and (availableRock >= neededRock and availableWater >= availableWater):
            print(f'{neededSand-availableSand} pasir.')
            return
        elif availableRock < neededRock and (availableSand >= neededSand and availableWater >= availableWater):
            print(f'{neededRock-availableRock} batu.')
            return
        elif availableWater < neededWater and (availableSand >= neededSand and availableRock >= availableRock):
            print(f'{neededWater-availableWater} air.')
            return
        
        elif (availableSand < neededSand and availableRock < neededRock) and availableWater >= availableWater:
            print(f'{neededSand-availableSand} pasir dan {neededRock-availableRock} batu.')
            return
        elif (availableSand < neededSand and availableWater < neededWater) and availableRock >= availableRock:
            print(f'{neededSand-availableSand} pasir dan {neededWater-availableWater} air.')
            return
        elif (availableRock < neededRock and availableWater < neededWater) and availableSand >= availableSand:
            print(f'{neededRock-availableRock} batu dan {neededWater-availableWater} air.')
            return
        
        else:
            print(f'{neededSand-availableSand} pasir, {neededRock-availableRock} batu, dan {neededWater-availableWater} air.')
            return
    
    else:
        row = 0
        countNone = 0
        if countData(data_candi) <= 100:
            for i in range(countJinPembangun):
                while data_candi[row][0] != None and data_candi[row][0] != '':
                    
                    row +=1
                
                if data_candi[row][0] is None:
                    countNone += 1
            # MENDAPATKAN ROW KOSONG PADA DATA_CANDI
            
                data_candi[row][0] = str(row)
                data_candi[row][1] = namesJinPembangun[lstOfRandomInteger[i]]
                data_candi[row][2] = str(matrixMaterialsNeeded[i][0])
                data_candi[row][3] = str(matrixMaterialsNeeded[i][1])
                data_candi[row][4] = str(matrixMaterialsNeeded[i][2])
                row += 1
                if row >= 100:
                    break #Tidak dimasukkan ke dalam data lagi karena jumlah candi sudah 100.
        
        
        
        data_bahan_bangunan[1][2] = str(int(data_bahan_bangunan[1][2]) - neededSand)
        data_bahan_bangunan[2][2] = str(int(data_bahan_bangunan[2][2]) - neededRock)
        data_bahan_bangunan[3][2] = str(int(data_bahan_bangunan[3][2]) - neededWater)
        
            
        
        
        print(f'Jin berhasil membangun total {countJinPembangun} candi.')
        

if __name__ == '__main__':
    data_user = read_csv('database/initial/user.csv')
    data_candi = read_csv('database/initial/candi.csv')
    data_bahan_bangunan = read_csv('database/initial/bahan_bangunan.csv')
    database= [data_user,data_candi,data_bahan_bangunan]
    print(data_bahan_bangunan)
    for i in range(10):
        batchkumpul_recursion(database, 3)
    print(data_bahan_bangunan)