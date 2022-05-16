import os
from PIL import Image

image_folder=r'your image folder'
if not 'output_folder' in os.listdir('.'):
    os.makedirs('output_folder')
for filename in os.listdir(image_folder):
    img=Image.open(f'{image_folder}{filename}')
    clean_name=os.path.splitext(filename)[0]
    img.save(f'./output_folder/'+clean_name+'.png','png')
print("Converted successfully")
























# import re
# if not 'pngs' in os.listdir('.'):
#     os.makedirs('pngs')

# for i in os.listdir('insta/jpgs/'):
#     name = re.findall('(.+)\.',i)
#     print(name[0])
#     img = Image.open('insta/jpgs/'+i)
#     img.save('./pngs/'+name[0]+'.png','png')

# print('All done!')