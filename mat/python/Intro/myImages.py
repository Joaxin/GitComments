picFormats = ['jpg', 'png', 'gif', 'jpeg', 'bmp', 'webp']
print('Plz enter a file name:')
file = input()
if file.lower().split(".")[-1] not in picFormats:
    print('Maybe not an image file. ')
else:
    print(file + ' is an image file.')