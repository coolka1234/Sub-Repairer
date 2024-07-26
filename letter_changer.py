import unidecode
import sys
import os

def convert_non_english_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    converted_content = unidecode.unidecode(content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(converted_content)


if __name__=='__main__':
    if len(sys.argv) < 2:
        print('Please provide the file path as an argument')
        sys.exit(1)
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print('File not found')
        sys.exit(1)
    convert_non_english_characters(file_path)
    print('File converted successfully')




