import json

def remove_duplicate_pairs(input_file, output_file):
    # Step 1: Read the JSON file
    with open(input_file, 'r') as file:
        # Step 2: Parse the JSON data
        data = json.load(file)

    # Step 3: Remove duplicate pairs
    unique_pairs = []
    seen_code = set()

    for item in data:
        code_type=item['type']
        code=item['code']
        pair = (code_type,code)
        if code not in seen_code:
            seen_code.add(code)
            unique_pairs.append(item)

    # Step 4: Write the modified data back to the JSON file
    with open(output_file, 'w',encoding='utf-8') as file:
        json.dump(unique_pairs, file, indent=2)

# Example usage:
input_json_file = 'chatgpt_codes2.json'

output_json_file = 'testing.json'

remove_duplicate_pairs(input_json_file, output_json_file)
