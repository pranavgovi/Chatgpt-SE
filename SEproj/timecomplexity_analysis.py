file_path = 'analysed_file2.json'

import re
import requests
import json
api_url="https://api.codepal.ai/v1/big-o-analyzer/query"
api_key = 'b7482f2d-67c6-44e4-941a-ed40a3e069b5'
main_list=[]
count=0
with open(file_path, 'r') as file:
    file_content = file.read()
    array_data = eval(file_content)
    for item in array_data:
        count+=1
        print(count)
        # print("language:",item["type"])
        # print("code:",item["code"])
        formatted_code = item["code"].replace('\n', '\\n')

        # Send a POST request to the API
        response = requests.post(
            api_url,
            headers={'Authorization': f'Bearer {api_key}'},
            data={'code': formatted_code}
        )

        # Handle the response

        answer=json.loads(response.text)
        print(answer)

        if answer["error"]!=None:
            continue

        else:


            pattern = re.compile(r'#### Time Complexity Analysis:(.*?)(?=\n#{2,})', re.DOTALL)

            matches = pattern.search(answer["result"])


            if matches:
                time_complexity_analysis = matches.group(1).strip()
                d={}
                d['type']=item['type']
                d["analysis"]=time_complexity_analysis



            else:
                d={}
                d['type']=item['type']
                d["analysis"]="Not found"
            print(d)
            with open('TimeComplexityAnalysis.txt', 'a', encoding='utf-8') as f:

                f.write(str(d) + '\n')




        # Append the response content to the file
print(main_list)

# def append_to_json_file(data_to_append, json_file):
#     # Step 1: Read the existing JSON file
#     with open(json_file, 'r') as f:
#         # Step 2: Parse the JSON data
#         existing_data = json.load(f)
#
#     # Step 3: Append your new data to the existing data
#     existing_data.extend(data_to_append)
#
#     # Step 4: Write the combined data back to the JSON file
#     with open(json_file, 'w') as f:
#         json.dump(existing_data, f, indent=2)

# Example usage:
# existing_json_file = 'API.json'
# print(len(main_list))
#
#
#
#
#
# def reduce_and_update_file(file_path, k):
#     # Read the JSON file
#     with open(file_path, 'r') as fl:
#         # Parse the JSON data
#         data = json.load(fl)
#
#     # Remove the first 'k' dictionaries
#     modified_data = data[k:]
#
#     # Write the modified data back to the same JSON file
#     with open(file_path, 'w') as fl:
#         json.dump(modified_data, fl, indent=2)
#
# # Example usage:
# json_file_path = 'analysed_file2.json'
# k_to_remove = len(main_list)  # Replace with the number of dictionaries you want to remove
#
# reduce_and_update_file(json_file_path, k_to_remove)
#
# append_to_json_file(main_list, existing_json_file)






