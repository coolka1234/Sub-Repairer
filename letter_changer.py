import unidecode

def convert_non_english_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    converted_content = unidecode.unidecode(content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(converted_content)
