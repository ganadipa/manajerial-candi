from typing import List

matrixData = List[List[str]]

def logout(database: List[matrixData]) -> None: 
    status_info = database[3][1]

    status_info[0] = 'False'
    status_info[1] = ''
    status_info[2] = ''


