def match_api_query(user_query):
    match = re.search(api_regex, user_query, flags=re.IGNORECASE)
    return match is not None

# Example usage
user_query = "How to use the API in Python?"
is_api_related = match_api_query(user_query)
print(f"Is API Related: {is_api_related}")
