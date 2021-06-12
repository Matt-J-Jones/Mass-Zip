import os
from os.path import basename
import zipfile




sub_folder=os.walk(".")
for folderName, subfolders, filenames in sub_folder:
    print(folderName)
    zip_file = zipfile.ZipFile(folderName+".zip", 'w')
    for filename in filenames:
        print("\t",filename)
        filePath = os.path.join(folderName, filename)
        if filePath != ".":
            zip_file.write(filePath, basename(filePath))
    zip_file.close()