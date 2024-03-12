
import os
import shutil
import json

root_folder = '/home/agamurian/gits/kerka_new/src/routes/events/'

for file in os.listdir(root_folder):
    if file.endswith('svelte'):
        shutil.move(file, file.replace('.svelte', '.svx'))
