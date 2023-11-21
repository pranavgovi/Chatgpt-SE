#response format
def process_api_request(request_data, response_format="json"):
    # Process the request and generate response in the specified format
    if response_format.lower() == "json":
        # Generate JSON response
        response = {"data": "your_data"}
    elif response_format.lower() == "xml":
        # Generate XML response
        response = "<data>your_data</data>"
    else:
        # Default to JSON
        response = {"data": "your_data"}
    
    return response


request_data = {...}
chosen_format = "XML"  # User-specified format
api_response = process_api_request(request_data, response_format=chosen_format)
