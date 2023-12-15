# Assuming you have a list already defined
my_list = []
import re
# Path to your text file
text_file_path = 'TimeComplexityAnalysis.txt'
dict={}
tc={}
dict_python = {}
dict_java = {}
dict_javascript = {}
dict_ruby = {}
dict_c={}
# Read each line from the text file and append it to the list
with open(text_file_path, 'r') as file:
    for line in file:
        if line.strip()!='':
            my_list.append(line)  # Use strip() to remove leading and trailing whitespace

# Now, your list contains each line from the text file
for input_string in my_list:


    type_match = re.search(r"'type': '(.*?)'", input_string)
    if type_match:
        extracted_type = type_match.group(1)

    flip=0
    # Find the pattern 'O(any complexity)' using regex
    complexity_pattern_match = re.search(r'O\([^)]*\)', input_string)
    if complexity_pattern_match:
        extracted_complexity_pattern = complexity_pattern_match.group()


    else:

        flip=-1

    if extracted_type=='python':
        if flip!=-1:
            if extracted_complexity_pattern in dict_python:
                dict_python[extracted_complexity_pattern]+=1
            else:
                dict_python[extracted_complexity_pattern] = 1
        else:
            if "Need more information" in dict_python:
                dict_python["Need more information"]+=1
            else:
                dict_python["Need more information"] = 1
    if extracted_type=='javascript':
        if flip!=-1:
            if extracted_complexity_pattern in dict_javascript:
                dict_javascript[extracted_complexity_pattern]+=1
            else:
                dict_javascript[extracted_complexity_pattern] = 1
        else:
            if "Need more information" in dict_javascript:
                dict_javascript["Need more information"]+=1
            else:
                dict_javascript["Need more information"] = 1
    if extracted_type=='c':
        if flip!=-1:
            if extracted_complexity_pattern in dict_c:
                dict_c[extracted_complexity_pattern]+=1
            else:
                dict_c[extracted_complexity_pattern] = 1
        else:
            if "Need more information" in dict_c:
                dict_c["Need more information"]+=1
            else:
                dict_c["Need more information"] = 1
    if extracted_type=='ruby':
        if flip!=-1:
            if extracted_complexity_pattern in dict_ruby:
                dict_ruby[extracted_complexity_pattern]+=1
            else:
                dict_ruby[extracted_complexity_pattern] = 1
        else:
            if "Need more information" in dict_ruby:
                dict_ruby["Need more information"]+=1
            else:
                dict_ruby["Need more information"] = 1
    if extracted_type=='java':
        if flip!=-1:
            if extracted_complexity_pattern in dict_java:
                dict_java[extracted_complexity_pattern]+=1
            else:
                dict_java[extracted_complexity_pattern] = 1
        else:
            if "Need more information" in dict_java:
                dict_java["Need more information"]+=1
            else:
                dict_java["Need more information"] = 1


    if extracted_type in dict:

        dict[extracted_type]+=1
    else:
        dict[extracted_type]=1
    if flip!=-1:
        if extracted_complexity_pattern in tc:
            tc[extracted_complexity_pattern]+=1
        else:
            tc[extracted_complexity_pattern] = 1
    else:
        if "Need more information" in tc:
            tc["Need more information"]+=1
        else:
            tc["Need more information"]=1
print("")
print("Languages split")
sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)

# Iterate over sorted items and print each line
for key, value in sorted_items:
    print(f"{key}: {value}")


print("")
print("Complexities")
sorted_items = sorted(tc.items(), key=lambda x: x[1], reverse=True)

# Iterate over sorted items and print each line
for key, value in sorted_items:
    print(f"{key}: {value}")



sorted_items = sorted(dict_ruby.items(), key=lambda x: x[1], reverse=True)
# Iterate over sorted items and print each line
print("")
print("Ruby")

for key, value in sorted_items:
    print(f"{key}: {value}")
print("")


sorted_items = sorted(dict_javascript.items(), key=lambda x: x[1], reverse=True)
print("Javascript")
# Iterate over sorted items and print each line
for key, value in sorted_items:
    print(f"{key}: {value}")


sorted_items = sorted(dict_java.items(), key=lambda x: x[1], reverse=True)
print("")
print("Java")
# Iterate over sorted items and print each line
for key, value in sorted_items:
    print(f"{key}: {value}")
print("")
print("C")
sorted_items = sorted(dict_c.items(), key=lambda x: x[1], reverse=True)
for key, value in sorted_items:
    print(f"{key}: {value}")

print("")

print("PYTHON")
sorted_items = sorted(dict_python.items(), key=lambda x: x[1], reverse=True)
for key, value in sorted_items:
    print(f"{key}: {value}")
