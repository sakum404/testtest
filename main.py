import os
import pandas as pd

def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append((root, file))
    return file_list

def save_to_excel(file_list, excel_file):
    df = pd.DataFrame(file_list, columns=['folder', 'file_name'])
    df['extension'] = df['file_name'].str.rsplit('.', 1).str[-1]
    df.insert(0, 'row_number', range(1, len(df) + 1))
    df.to_excel(excel_file, index=False)

if __name__ == '__main__':
    path = './'
    file_list = get_file_list(path)
    save_to_excel(file_list, 'result.xlsx')
