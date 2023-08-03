import re 
import json
def clean(lines):
    data = []    
    n_lin=[]   
    mid_data=[] 
    pre_data=[]
    final_data =[]
    for line in lines:
            input_line=line.rstrip()
            input_line = re.sub(r'\\[u]\S\S\S\S[s]', "", input_line)
            input_line = re.sub(r'\\[u]\S\S\S\S', "", input_line)
            data.append(input_line)
    for element in data:
        n_lin.append(element + "\n")
    for line in n_lin:
        input_line=line.rstrip()
        input_line = input_line.replace('.','\n')
        mid_data.append(input_line)
    for element in mid_data:
        pre_data.append(element + "\n")
    for line in pre_data:
        input_line=line.rstrip()
        input_line = re.sub(r"(@[A-Za-z0-9]+ |)|([^0-9A-Za-z | ,| \ \t])|^rt|http+?", "", input_line)
        if(len(input_line) > 55):
            final_data.append(input_line+'.')
    data=json.dumps(final_data,indent=8)
    return data
