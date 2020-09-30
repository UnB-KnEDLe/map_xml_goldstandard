import os
import csv
import shutil

original_path = "dodfs_original/"
preprocessed_path = "dodfs_renamed/"

dodfs_xml = os.listdir(original_path)

i = 1;

mapping = {}

for file_xml in dodfs_xml:
    renm_path = "{:d}".format(i)+".xml"
    mapping[file_xml] = renm_path
    
    o_path = original_path+file_xml
    renm_path = preprocessed_path+"{:d}".format(i)+".xml"
    
    print("cp "+o_path+"  "+renm_path)
    os.popen("cp "+o_path+" "+renm_path)
    
    i = i+1
    #os.rename(file_xml, preprocessed_path+"{:d}".format{i}+".xml")

#os.rename(old_file_name, new_file_name)

with open('mapeamento_xmls.csv', 'w') as f:
    for key in mapping.keys():
        f.write("%s,%s\n"%(key,mapping[key]))