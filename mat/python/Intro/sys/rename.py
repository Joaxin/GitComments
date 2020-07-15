import os
path = 'D:\\shortcuts\\ST3\\Packages\\Sublime Text\\\Packages'
i = 1
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        # if the destination file exists

        new_name = file.replace(file, "%d_%s_encrypted" % (i, file.split('.')[0]))
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
        i += 1
