#! python3
# backupToZip.py
# Copies an entire folder and its contents into
# a zip file whose filename increments.
'''
假定你正在做一个项目，它的文件保存在 C:\AlsPythonBook 文件夹中。你担心工作
会丢失，所以希望为整个文件夹创建一个 ZIP 文件，作为“快照”。你希望保存不同的版
本，希望 ZIP 文件的文件名每次创建时都有所变化。例如 AlsPythonBook_1.zip、
AlsPythonBook_2.zip、AlsPythonBook_3.zip，等等。你可以手工完成，但这有点烦人，
而且可能不小心弄错 ZIP 文件的编号。运行一个程序来完成这个烦人的任务会简单得多。 
针对这个项目，打开一个新的文件编辑器窗口，将它保存为 backupToZip.py。
'''

import zipfile, os, sys

def backupToZip(folder):
    # Backup the entire contents of "folder" into a zip file.

    ## 这里我们不需要绝对路径
    # folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should used based on 
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the zip file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

if len(sys.argv) >=2:
    backupToZip(sys.argv[1])
