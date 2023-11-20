file_path = './final.json'
import requests
import json
api_url="https://api.codepal.ai/v1/big-o-analyzer/query"
api_key = 'b4d1af4a-af14-46af-8298-dcfb5e976b08'
count=0
with open(file_path, 'r') as file:
    file_content = file.read()
    array_data = eval(file_content)
    for item in array_data:
        count+=1
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
        output_file_path = 'API_output.txt'
        answer=json.loads(response.text)
        print(answer)

        # Append the response content to the file
        # with open(output_file_path, 'a') as output_file:
        #     output_file.write(answer["result"] + '\n')
        if count==1:
            break



