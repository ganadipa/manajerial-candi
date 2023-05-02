import os
os.chdir(os.path.dirname(__file__))

def read_csv(csv_file, delimiter = ';'):
    data_matrix = [['' for i in range(10)] for i in range(1000)]
    
    with open(csv_file, 'r') as file:
        
        row_number = 0
        col_number = 0
        
        current_char = file.read(1)
        datum = ''
        while current_char != '':
            
            if current_char == delimiter:
                data_matrix[row_number][col_number] = datum
                
                datum = ''
                col_number += 1
            
            elif current_char == '\n':
                data_matrix[row_number][col_number] = datum
                
                datum = ''
                col_number = 0
                row_number += 1
                
            else:
                datum = datum + current_char
            
            current_char = file.read(1) # Update the current character to the next one and iterate again.
    
    return data_matrix



def write_csv(csv_file, data):
    row = 0
    f = open(csv_file, 'w')
    write_csv_helper(f, data, row)
    f.close()        
            
def write_csv_helper(f, data, row = 0):
    col = 0
    cellData = data[row][0]
    if cellData == '': # BASE CASE
        return
    
    if cellData is None:
        write_csv_helper(f, data, row+1)
    else:
        f.write(cellData)
        col += 1
        cellData = data[row][col]
        while cellData != '':
            f.write(';')
            f.write(cellData)
            col += 1
            cellData = data[row][col]
        f.write('\n')
        write_csv_helper(f, data, row+1)
            
        
if __name__ == '__main__':
    data_user = read_csv('save/initial/user.csv')
    write_csv('save/15-04-2023/user.csv',data_user )
    
        