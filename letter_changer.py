from math import e
import unidecode
import sys
import os
import chardet
from pathlib import Path

def convert_non_english_characters(file_path):
    '''Convert non-english characters to english characters'''
    encoding = predict_encoding(file_path)
    print(f'Encoding: {encoding}')
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
    converted_content = unidecode.unidecode(content)
    
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(converted_content)

def predict_encoding(file_path: Path, n_lines: int=20) -> str:
    '''Predict a file's encoding using chardet'''

    with Path(file_path).open('rb') as f:
        rawdata = b''.join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)['encoding']

def change_polish_letters(file_path):
    '''Change polish letters to english letters'''
    # encoding = predict_encoding(file_path)
    # print(f'Encoding: {encoding}')
    with open(file_path, 'r', encoding='cp1250') as file:
        content = file.read()
    content = content.replace('ą', 'a').replace('ć', 'c').replace('ę', 'e').replace('ł', 'l').replace('ń', 'n').replace('ó', 'o').replace('ś', 's').replace('ż', 'z').replace('ź', 'z')
    with open(file_path, 'w') as file:
        file.write(content)
if __name__=='__main__':
    if len(sys.argv) < 2:
        print('Please provide the file path as an argument')
        sys.exit(1)
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print('File not found')
        sys.exit(1)
    change_polish_letters(file_path)
    print('File converted successfully')




