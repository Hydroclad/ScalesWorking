      
import os

list_of_files = os.listdir(path="C:\Text Editors\strat_editor")

list_of_files = list_of_files[:-2]

strategic_regions = len(list_of_files)

primary = '215.txt'

def primary_list(primary):
    # Opens the primary file, and returns a list of provinces therein
    with open(primary, 'r') as file1:
        
        prime_content = file1.readlines()
            
        for prime_i in range(0, len(prime_content)):
            
            if 'province' in prime_content[prime_i]:
                    
                prime_prov_list = prime_content[prime_i+1].split()
                
                return prime_prov_list

def remove_if_in_others(prime_prov_list):
    # Removes all provinces in primary text file from all others
    
    for i in range(0, strategic_regions):
        
        if list_of_files[i] != primary:
        
            with open(list_of_files[i], 'r') as file2:
                    
                content = file2.readlines()    
            
            for j in range(0, len(content)):
                
                if 'province' in content[j]:
                        
                    prov_list = content[j+1].split()
            
                    for k in range(0, len(prov_list)):
                        
                        if prov_list[k] in prime_prov_list:
                            
                            prime_prov_list.remove(prov_list[k])
    return prime_prov_list

def editor(edited_prov_list, editee):
    with open(editee, 'r') as edit_file1:
        edit_content = edit_file1.readlines()
        
        for edit_i in range(0, len(edit_content)):
            
            if 'province' in edit_content[edit_i]:
                    
                edit_content[edit_i+1] = '\t' + '\t' + " ".join(edited_prov_list) + '\n'     
    
    with open(editee, 'w') as edit_file2:
        edit_file2.writelines(edit_content)
    
    return
    

def copy_removal(region):
    with open(region, 'r') as file_cop1:
        
        copy_content = file_cop1.readlines()
        
        for copy_i in range(0, len(copy_content)):
            
            if 'province' in copy_content[copy_i]:
                    
                no_copy_provs = set(copy_content[copy_i+1].split())
                copy_content[copy_i+1] = '\t' + '\t' + " ".join(list(no_copy_provs)) + '\n'
                
    with open(region, 'w') as file_cop2:
        file_cop2.writelines(copy_content)
         
    return

result = remove_if_in_others(primary_list(primary))

editor(result, primary)

for regions in range(0, strategic_regions):
    copy_removal(list_of_files[regions])