import os
import csv
import shutil
import re

original_path = "xml/"
preprocessed_path = "xml2/"

dodfs_xml = os.listdir(original_path)

for file_xml in dodfs_xml:
    
    opath = original_path+file_xml;
    
    print(opath)
    
    filex = open(opath, 'r')
  
    renm_path = preprocessed_path+file_xml
  
    text = filex.read()
    
    text = re.sub('hierarqui_lotacao', 'hierarquia_lotacao', text)
    
    filex.seek(0)
    
    text = re.sub('matricula_SIAPE', 'matricula_siape', text)
    
    filex.seek(0)
    
    text = re.sub('especialiade', 'especialidade', text)
    
    filex.seek(0)
    
    #filedata.replace('hierarqui_lotacao', 'hierarquia_lotacao')
    
    #filedata.replace('matricula_SIAPE', 'matricula_siape')
    
    #filedata.replace('especialiade', 'especialidade')

    # Write the file out again
    filex = open(renm_path, 'w')
    
    filex.write(text)
  
  