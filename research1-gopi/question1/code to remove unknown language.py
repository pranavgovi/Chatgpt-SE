import re

def contains_chinese_or_japanese(text):
    # Use regular expression to check if the text contains Chinese or Japanese characters
    chinese_japanese_pattern = re.compile('[\u4e00-\u9fa5ぁ-んァ-ヶ]')
    return bool(chinese_japanese_pattern.search(text))

def preprocess_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
        l=[]

    # Remove lines containing Chinese or Japanese characters
        for line in lines:
            if line not in l:
                l.append(line)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(l)


if _name_ == "_main_":
    input_file_path = 'output.txt'
    output_file_path = 'main_op.txt'

    preprocess_text(input_file_path, output_file_path)