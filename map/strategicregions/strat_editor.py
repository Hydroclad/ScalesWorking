      
import os

list_of_files = os.listdir(path="C:\Text Editors\strat_editor")

list_of_files = list_of_files[:-2]

strategic_regions = len(list_of_files)

primary = '314-West Frozen Islands.txt'

def primary_list(primary):
    # Opens the primary file, and returns a list of provinces therein
    with open(primary, 'r') as file1:
        
        prime_content = file1.readlines()
            
        for prime_i in range(0, len(prime_content)):
            
            if 'province' in prime_content[prime_i]:
                    
                prime_prov_list = prime_content[prime_i+1].split()
                
                return prime_prov_list

def remove_from_others(prime_prov_list):
    # Removes all provinces in primary text file from all others
    
    for i in range(0, strategic_regions):
        
        if list_of_files[i] != primary:
        
            with open(list_of_files[i], 'r') as file2:
                    
                content = file2.readlines()    
            
            for j in range(0, len(content)):
                
                if 'province' in content[j]:
                        
                    prov_list = content[j+1].split()
            
                    for k in range(0, len(prime_prov_list)):
                        
                        if prime_prov_list[k] in prov_list:
                            
                            prov_list.remove(prime_prov_list[k])
                            
                    content[j+1] = '\t' + " ".join(prov_list) + '\n'
                
            with open(list_of_files[i], 'w') as file3:
                
                file3.writelines(content)
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

#remove_from_others(primary_list('77-Northpost.txt'))
copy_removal('40.txt')