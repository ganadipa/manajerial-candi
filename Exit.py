import sys
import Save
from typing import List, Optional
matrixData = List[List[str]]
def exit(data: List[matrixData], userInput:Optional[str] = ''): #RECURSION
    if userInput == 'Y' or userInput == 'y':
        Save.save(data)
    elif userInput == 'N' or userInput == 'n':
        sys.exit()

    print('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ', end = '')
    userInput = input()
    
    exit(data, userInput)
    