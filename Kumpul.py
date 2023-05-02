import LCG
import os
os.chdir(os.path.dirname(__file__))

from typing import List
matrixData = List[List[str]]

def kumpul(database: List[matrixData])-> None:
    # KAMUS LOKAL
    # rock, sand, water: variable -- type: integer
    
    data_bahan_bangunan = database[2]
    materialsCollected = LCG.randsample(3, 0, 5)
    sandCollected = materialsCollected[0]
    rockCollected = materialsCollected[1]
    waterCollected = materialsCollected[2]

    
    data_bahan_bangunan[1][2] = str(int(data_bahan_bangunan[1][2]) + sandCollected)
    data_bahan_bangunan[2][2] = str(int(data_bahan_bangunan[2][2]) + rockCollected)
    data_bahan_bangunan[3][2] = str(int(data_bahan_bangunan[3][2]) + waterCollected)

    # updateCSV('bahan_bangunan.csv', data_bahan_bangunan)
    print(f'Jin menemukan {sandCollected} pasir, {rockCollected} batu, dan {waterCollected} air.')
