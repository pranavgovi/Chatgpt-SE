 #code for constructing regex patterns
import re

api_terms = [ "API", "API CALL","API ECONOMY","API GATEWAY","API INTEGRATION","API KEYS","API LIFECYCLE","API Layer","API Portal","API Request","API Security","Apigee","APIsec","Application","Burp Suite","CI/CD","CRUD","Cache","Client","DDoS","DevOps","DevSecOps","Developer Portal","External APIs","Framework","GET Method","GraphQL","HTTP Methods","JSON","Logic Flaw","Microservices","OWASP","Parameters","REST","Red Teams","SDK","SDLC","SOAP","SQL Injection","Webhook","ZAP"]
regex_patterns = [re.escape(API) for API in api_terms]
api_regex = "|".join(regex_patterns)
