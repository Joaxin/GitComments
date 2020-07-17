for %%X in (*) do "c:\Program Files\7-Zip\7z.exe" a -ttar "%%X.tar" "%%X\"
for %%X in (*.tar) do "c:\Program Files\7-Zip\7z.exe" a -tgzip "%%X.gz" "%%X"