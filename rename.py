import os

path = 'nomes/'
i = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path, filename + '.xml'))
    i = i +1